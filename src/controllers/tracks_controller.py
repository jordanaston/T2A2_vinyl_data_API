from flask import Blueprint, jsonify, request, abort
from main import db
from models.tracks import Track
from schemas.track_schema import track_schema, tracks_schema

tracks = Blueprint('tracks', __name__, url_prefix="/tracks")

# The GET routes endpoint
@tracks.route("/", methods=["GET"])
def get_tracks():
    # get all the users from the database table
    track_list = Track.query.all()
    # Convert the cards from the database into a JSON format and store them in result
    result = tracks_schema.dump(track_list)
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
def delete_track(id):
    # #get the user id invoking get_jwt_identity
    # user_id = get_jwt_identity()
    # #Find it in the db
    # user = User.query.get(user_id)
    # #Make sure it is in the database
    # if not user:
    #     return abort(401, description="Invalid user")
    # # Stop the request if the user is not an admin
    # if not user.admin:
    #     return abort(401, description="Unauthorised user")
    # find the card
    track = Track.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not Track:
        return abort(400, description= "Track doesn't exist")
    #Delete the card from the database and commit
    db.session.delete(track)
    db.session.commit()
    #return the card in the response
    return jsonify(track_schema.dump(track))
   