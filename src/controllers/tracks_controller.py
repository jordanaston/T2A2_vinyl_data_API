from flask import Blueprint, jsonify, request, abort
from main import db
from models.tracks import Track
from models.collections import Collection
from models.records import Record
from schemas.track_schema import track_schema, tracks_schema 
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import admin_required

# Create a Flask Blueprint for the /tracks endpoint
tracks = Blueprint('tracks', __name__, url_prefix="/tracks")

# The GET routes endpoint returning list of all tracks in the database (admin authorized only)
@tracks.route("/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_tracks():
    # Get all the tracks from the database table
    track_list = Track.query.all()
    # Convert the tracks from the database into a JSON format and store them in result
    result = tracks_schema.dump(track_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a single track in the database by id (admin authorized only)
@tracks.route("/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_track(id):
    # Find the track in the database filtering by id
    track = Track.query.filter_by(id=id).first()
    # Stop the request if the track does not exist
    if not track:
        return abort(400, description= "Track does not exist")
    # Convert the track from the database into a JSON format and store them in result
    result = track_schema.dump(track)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a list of all tracks related to the user (user authorized only)
@tracks.route("/user/tracks/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_user_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get all the tracks related to the user from the database table
    track_list = Track.query \
        .join(Record) \
        .join(Collection) \
        .filter(Track.record_id==Record.id, Collection.user_id==user_id) \
        .all()
    # Return an error if no tracks relate to the user
    if not track_list:
        return abort(401, description="No tracks related to this user")
    # Convert the track from the database into a JSON format and store them in result
    result = tracks_schema.dump(track_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a specific track created by a user
@tracks.route("/user/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_user_track(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the track with the specified ID from the database
    track = Track.query.filter_by(id=id).first()
    # Return an error if the track doesn't exist
    if not track:
        return abort(400, description= "Track does not exist")
    # Get the relationship between the track with the specified ID and the current user
    relationship = Record.query \
        .join(Track) \
        .join(Collection) \
        .filter(Track.id == id, Collection.user_id == user_id, Collection.record_id == Record.id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Convert the track from the database into a JSON format and store them in result
    result = track_schema.dump(track)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning any tracks created by the user with a specifc track_title, bpm or key
# Remember when searching for the 'key' of a track with a sharp (#), replace "# " with "%23%20". EG: A# Major = A%23%20Major
@tracks.route("/search", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def search_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Create an empty list in case the query string is not valid
    tracks_list = []
    # Check if a "track_title" query parameter was included in the request
    if request.args.get('track_title'):
    # If a "track_title" parameter was provided, filter the Track query by track_title value
        tracks_list = Track.query.filter_by(track_title= request.args.get('track_title'))
    # Check if a "bpm" query parameter was included in the request
    elif request.args.get('bpm'):
    # If a "bpm" parameter was provided, filter the Track query by bpm value
        tracks_list = Track.query.filter_by(bpm= request.args.get('bpm'))
    # Check if a "key" query parameter was included in the request
    elif request.args.get('key'):
    # If a "key" parameter was provided, filter the Track query by key value
        tracks_list = Track.query.filter_by(key= request.args.get('key'))
    # Filter the tracks by user
    tracks_list = tracks_list.join(Record, Track.record_id == Record.id)\
                            .join(Collection, Record.id == Collection.record_id)\
                            .filter(Collection.user_id == user_id)\
                            .all()
    # Check if the track searched for is in the user's collection, if not return a 400 error with a message.
    if not tracks_list:
        return abort(400, description= "Not found in your collection")  
    # Convert the tracks from the database into a JSON format and store them in result
    result = tracks_schema.dump(tracks_list)
    # Return the data in JSON format
    return jsonify(result)  


# The POST routes endpoint; any logged in user can post a new track to the database as long as the record_id is related to the user_id
@tracks.route("/", methods=["POST"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def create_track():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Load track data from the request, create a new Track object, and set its attributes
    track_fields = track_schema.load(request.json)
    new_track = Track()
    new_track.track_title = track_fields["track_title"]
    new_track.bpm = track_fields["bpm"]
    new_track.key = track_fields["key"]
    # Check if the track_id exists in the Track table, return an error if not located
    if not Track.query.get(track_fields["record_id"]):
        return abort(400, description="Invalid record_id (not in database)")
    # Check if the record_id is related to the user_id
    if not Collection.query.filter_by(user_id=user_id, record_id=track_fields["record_id"]).first():
        return abort(400, description="Unauthorized user (record_id not related)")
    # Set the record_id attribute if authorized
    new_track.record_id = track_fields["record_id"]
    # Add to the database and commit
    db.session.add(new_track)
    db.session.commit()
    # Return the track in the response
    return jsonify(track_schema.dump(new_track))


# The PUT routes endpoint; authorized users who created the track can update the track data keeping track id in tact 
@tracks.route("/<int:id>/", methods=["PUT"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def update_tracks(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the relationship between the track with the specified ID and the current user
    relationship = Record.query \
        .join(Track) \
        .join(Collection) \
        .filter(Track.id == id, Collection.user_id == user_id, Collection.record_id == Record.id) \
        .first()
    # Stop the request if the user is unauthorized or the track does not exist
    if not relationship:
        return abort(401, description="Unauthorized user or track does not exist")
    # Get the track with the specified ID from the database
    track = Track.query.filter_by(id=id).first()
    # Load track data from the request, and update the attributes
    track_fields = track_schema.load(request.json)
    track.track_title = track_fields["track_title"]
    track.bpm = track_fields["bpm"]
    track.key = track_fields["key"]
    # Commit to the database
    db.session.commit()
    # Return the track in the response
    return jsonify(track_schema.dump(track))


# The DELETE routes endpoint; users who are authorized can delete tracks they have created
@tracks.route("/<int:id>/", methods=["DELETE"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def delete_track(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the relationship between the track with the specified ID and the current user
    relationship = Record.query \
        .join(Track) \
        .join(Collection) \
        .filter(Track.id == id, Collection.user_id == user_id, Collection.record_id == Record.id) \
        .first()
    # Stop the request if the user is unauthorized or the track does not exist
    if not relationship:
        return abort(401, description="Unauthorized user or the track does not exist")
    # Find the track in the database by id
    track = Track.query.filter_by(id=id).first()
    # Delete the track from the database and commit
    db.session.delete(track)
    db.session.commit()
    # Return the track in the response
    return jsonify(track_schema.dump(track))
   