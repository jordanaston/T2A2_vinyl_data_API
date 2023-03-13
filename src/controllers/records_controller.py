from flask import Blueprint, jsonify, request, abort
from main import db
from models.records import Record
from models.users import User
from models.artists import Artist
from schemas.record_schema import record_schema, records_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

records = Blueprint('records', __name__, url_prefix="/records")

# The GET routes endpoint to get all records
@records.route("/", methods=["GET"])
def get_records():
    # get all the users from the database table
    record_list = Record.query.all()
    # Convert the cards from the database into a JSON format and store them in result
    result = records_schema.dump(record_list)
    # return the data in JSON format
    return jsonify(result)

# The GET routes endpoint for a single record
@records.route("/<int:id>/", methods=["GET"])
def get_record(id):
    record = Record.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not record:
        return abort(400, description= "Record does not exist")
    # Convert the cards from the database into a JSON format and store them in result
    result = record_schema.dump(record)
    # return the data in JSON format
    return jsonify(result)


# The POST route endpoint
@records.route("/", methods=["POST"])
@jwt_required()
def create_record():
    # #Create a new record
    record_fields = record_schema.load(request.json)

    # get the id from jwt
    user_id = get_jwt_identity()
    new_record = Record()
    new_record.album_title = record_fields["album_title"]
    new_record.rpm = record_fields["rpm"]
    # new_record.user_id = record_fields["user_id"]

    # Use that id to set the ownership of the card
    new_record.user_id = user_id

    new_record.artist_id = record_fields["artist_id"]
    # add to the database and commit
    db.session.add(new_record)
    db.session.commit()
    # #return the card in the response
    return jsonify(record_schema.dump(new_record))


# Finally, we round out our CRUD resource with a DELETE method

@records.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Find the record
    record = Record.query.filter_by(id=id).first()
    # Return an error if the card doesn't exist
    if not Record:
        return abort(400, description= "Record doesn't exist")
    # Delete the record from the database and commit
    db.session.delete(record)
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(record))