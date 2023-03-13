from flask import Blueprint, jsonify, request, abort
from main import db
from models.tracks import Track
from models.users import User
from models.collections import Collection
from models.records import Record
from schemas.track_schema import track_schema, tracks_schema 
from flask_jwt_extended import jwt_required, get_jwt_identity

tracks = Blueprint('tracks', __name__, url_prefix="/tracks")

# The GET routes endpoint for all tracks (admin required)
@tracks.route("/", methods=["GET"])
@jwt_required()
def get_tracks():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # get all the users from the database table
    track_list = Track.query.all()

    # Convert the cards from the database into a JSON format and store them in result
    result = tracks_schema.dump(track_list)
    # return the data in JSON format
    return jsonify(result)


# # The GET routes endpoint for a single tracks
# @tracks.route("/<int:id>/", methods=["GET"])
# def get_track(id):
#     track = Track.query.filter_by(id=id).first()
#     #return an error if the card doesn't exist
#     if not track:
#         return abort(400, description= "Track does not exist")
#     # Convert the cards from the database into a JSON format and store them in result
#     result = track_schema.dump(track)
#     # return the data in JSON format
#     return jsonify(result)

# The GET routes endpoint for specific tracks created by a user
@tracks.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_track(id):
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    
    if not user:
        return abort(401, description="Invalid user")

    track = Track.query.filter_by(id=id).first()
    
    if not track:
        return abort(400, description= "Track does not exist")
    
    relationship = Track.query \
        .join(Record) \
        .join(Collection) \
        .filter(Track.id==id, Collection.user_id == user_id) \
        .first()
    
    if not relationship:
        return abort(401, description="Unauthorised user")
    
    # Convert the track from the database into a JSON format and store them in result
    result = track_schema.dump(track)
    # return the data in JSON format
    return jsonify(result)




# The POST route endpoint
@tracks.route("/", methods=["POST"])
def create_track():
    # #Create a new table
    track_fields = track_schema.load(request.json)

    new_track = Track()
    new_track.track_title = track_fields["track_title"]
    new_track.bpm = track_fields["bpm"]
    new_track.key = track_fields["key"]
    new_track.record_id = track_fields["record_id"]
    
    # add to the database and commit
    db.session.add(new_track)
    db.session.commit()
    #return the card in the response
    return jsonify(track_schema.dump(new_track))


# Finally, we round out our CRUD resource with a DELETE method
@tracks.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_track(id):
    # get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    
    # find the track
    track = Track.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not Track:
        return abort(400, description= "Track doesn't exist")
    #Delete the track from the database and commit
    db.session.delete(track)
    db.session.commit()
    #return the track in the response
    return jsonify(track_schema.dump(track))
   