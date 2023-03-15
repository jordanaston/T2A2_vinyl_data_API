from flask import Blueprint, jsonify, request, abort
from main import db
from models.records import Record
from models.collections import Collection
from models.users import User
from models.artists import Artist
from schemas.record_schema import record_schema, records_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a Flask Blueprint for the /records endpoint
records = Blueprint('records', __name__, url_prefix="/records")

# The GET routes endpoint returning list of all records in the database (admin authorized only)
@records.route("/", methods=["GET"])
@jwt_required()
def get_records():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Get all the records from the database table
    record_list = Record.query.all()
    # Convert the records from the database into a JSON format and store them in result
    result = records_schema.dump(record_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a single record in the database (admin authorized only)
@records.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Find the record in the database by id
    record = Record.query.filter_by(id=id).first()
    # Stop the request if the record does not exist
    if not record:
        return abort(400, description= "Record does not exist")
    # Convert the record from the database into a JSON format and store them in result
    result = record_schema.dump(record)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a list of all records related to the user (user authorized only)
@records.route("/user/records/", methods=["GET"])
@jwt_required()
def get_user_records():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Get all the records related to the user from the database table
    record_list = Record.query \
        .join(Collection) \
        .filter(id==id, Collection.user_id==user_id) \
        .distinct() \
        .all()
    # Stop the request if the user is unauthorized
    if not record_list:
        return abort(401, description="Unauthorized user")
    # Convert the records from the database into a JSON format and store them in result
    result = records_schema.dump(record_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a specific record created by a user
@records.route("/user/<int:id>/", methods=["GET"])
@jwt_required()
def get_user_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Get the record with the specified ID from the database
    record = Record.query.filter_by(id=id).first()
    # Return an error if the record doesn't exist
    if not record:
        return abort(400, description= "Record does not exist")
    # Get the relationship between the record with the specified ID and the current user
    relationship = Record.query \
        .join(Collection) \
        .filter(Collection.record_id == id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Convert the record from the database into a JSON format and store them in result
    result = record_schema.dump(record)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning any records created by the user with a specifc album_title, rpm
@records.route("/search", methods=["GET"])
@jwt_required()
def search_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Create an empty list in case the query string is not valid
    records_list = []
    # Check if a "album_title" query parameter was included in the request
    if request.args.get('album_title'):
    # If an "album_title" parameter was provided, filter the Record query by album_title value
        records_list = Record.query.filter_by(album_title= request.args.get('album_title'))
    # Check if an "rpm" query parameter was included in the request
    elif request.args.get('rpm'):
    # If an "rpm" parameter was provided, filter the Record query by rpm value
        records_list = Record.query.filter_by(rpm= request.args.get('rpm'))
    # Filter the records by user
    records_list = records_list.join(Collection, Record.id == Collection.record_id)\
                            .filter(Collection.user_id == user_id)\
                            .all()     
    # Check if the record searched for is in the user's collection, if not return a 400 error with a message.
    if not records_list:
        return abort(400, description= "Not found in your collection")            
    # Convert the records from the database into a JSON format and store them in result
    result = records_schema.dump(records_list)
    # Return the data in JSON format
    return jsonify(result)  


# The POST route endpoint, any logged in user can post a new record to the database
@records.route("/", methods=["POST"])
@jwt_required()
def create_record():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Load record data from the request, create a new Record object, and set its attributes
    record_fields = record_schema.load(request.json)
    new_record = Record()
    new_record.album_title = record_fields["album_title"]
    new_record.rpm = record_fields["rpm"]
    # Check if the artist_id exists in the Artist table
    if not Artist.query.get(record_fields["artist_id"]):
        return abort(400, description="Invalid artist_id")
    new_record.artist_id = record_fields["artist_id"]
    # Add to the database and commit
    db.session.add(new_record)
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(new_record))


# The PUT route endpoint, authorized users who created the record can update the record data keeping record id in tact 
@records.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the record with the specified ID from the database
    record = Record.query.filter_by(id=id).first()
    # Return an error if the record doesn't exist
    if not Record:
        return abort(400, description= "Record does not exist")
    # Get the relationship between the record with the specified ID and the current user
    relationship = Record.query \
        .join(Collection) \
        .filter(Collection.record_id == id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Load record data from the request, and update the attributes
    record_fields = record_schema.load(request.json)
    record.album_title = record_fields["album_title"]
    record.rpm = record_fields["rpm"]
    # Commit to the database
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(record))


# The DELETE route endpoint, users who are authorized can delete records they have created
@records.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the database
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Get the relationship between the record with the specified ID and the current user
    relationship = Record.query \
        .join(Collection) \
        .filter(Collection.record_id == id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Find the record
    record = Record.query.filter_by(id=id).first()
    # Return an error if the record doesn't exist
    if not Record:
        return abort(400, description= "Record doesn't exist")
    # Delete the record from the database and commit
    db.session.delete(record)
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(record))
