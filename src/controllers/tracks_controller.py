from flask import Blueprint, jsonify, request, abort
from main import db
from models.tracks import Track
from models.users import User
from models.collections import Collection
from models.records import Record
from schemas.track_schema import track_schema, tracks_schema 
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a Flask Blueprint for the /tracks endpoint
tracks = Blueprint('tracks', __name__, url_prefix="/tracks")

# The GET routes endpoint returning list of all records in the database (admin authorized only)
@tracks.route("/", methods=["GET"])
@jwt_required()
def get_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Get all the tracks from the database table
    track_list = Track.query.all()
    # Convert the tracks from the database into a JSON format and store them in result
    result = tracks_schema.dump(track_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a single track in the database (admin authorized only)
@tracks.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_track(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
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
@jwt_required()
def get_user_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    #  Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Get all the tracks related to the user from the database table
    track_list = Track.query \
        .join(Record) \
        .join(Collection) \
        .filter(Track.record_id==Record.id, Collection.user_id==user_id) \
        .distinct() \
        .all()
    # Check if there are tracks related to the user
    if len(track_list) == 0:
        return abort(401, description="No tracks related to the user")
    # Stop the request if the user is unauthorized
    if not track_list:
        return abort(401, description="Unauthorized user")
    # Convert the track from the database into a JSON format and store them in result
    result = tracks_schema.dump(track_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a specific track created by a user
@tracks.route("/user/<int:id>/", methods=["GET"])
@jwt_required()
def get_user_track(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
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
@jwt_required()
def search_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
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


# The POST route endpoint, any logged in user can post a new track to the database
@tracks.route("/", methods=["POST"])
@jwt_required()
def create_track():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Load track data from the request, create a new Track object, and set its attributes
    track_fields = track_schema.load(request.json)
    new_track = Track()
    new_track.track_title = track_fields["track_title"]
    new_track.bpm = track_fields["bpm"]
    new_track.key = track_fields["key"]
    # Check if the track_id exists in the Track table
    if not Track.query.get(track_fields["record_id"]):
        return abort(400, description="Invalid record_id")
    new_track.record_id = track_fields["record_id"]
    # Add to the database and commit
    db.session.add(new_track)
    db.session.commit()
    # Return the track in the response
    return jsonify(track_schema.dump(new_track))


# The PUT route endpoint, authorized users who created the track can update the track data keeping track id in tact 
@tracks.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_tracks(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the track with the specified ID from the database
    track = Track.query.filter_by(id=id).first()
    # Return an error if the track doesn't exist
    if not Track:
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
    # Load track data from the request, and update the attributes
    track_fields = track_schema.load(request.json)
    track.track_title = track_fields["track_title"]
    track.bpm = track_fields["bpm"]
    # Commit to the database
    db.session.commit()
    # Return the track in the response
    return jsonify(track_schema.dump(track))


# The DELETE route endpoint, users who are authorized can delete tracks they have created
@tracks.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_track(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Get the relationship between the track with the specified ID and the current user
    relationship = Record.query \
        .join(Track) \
        .join(Collection) \
        .filter(Track.id == id, Collection.user_id == user_id, Collection.record_id == Record.id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Find the track
    track = Track.query.filter_by(id=id).first()
    # Return an error if the track doesn't exist
    if not Track:
        return abort(400, description= "Track doesn't exist")
    # Delete the track from the database and commit
    db.session.delete(track)
    db.session.commit()
    # Return the track in the response
    return jsonify(track_schema.dump(track))
   