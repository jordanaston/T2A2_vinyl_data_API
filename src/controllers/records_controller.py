from flask import Blueprint, jsonify, request, abort
from main import db
from models.records import Record
from models.collections import Collection
from models.artists import Artist
from schemas.record_schema import record_schema, records_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import admin_required
from sqlalchemy.orm import joinedload

# Create a Flask Blueprint for the /records endpoint
records = Blueprint('records', __name__, url_prefix="/records")

# The GET routes endpoint returning list of all records in the database (admin authorized only)
@records.route("/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_records():
    # Get all the records from the database table
    record_list = Record.query.all()
    # Convert the records from the database into a JSON format and store them in result
    result = records_schema.dump(record_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a single record by record_id
@records.route("/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_record(id):
    # Find the record in the database by id
    record = Record.query.filter_by(id=id).first()
    # Return an error if the record does not exist
    if not record:
        return abort(400, description= "Record does not exist")
    # Convert the record from the database into a JSON format and store them in result
    result = record_schema.dump(record)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a list of all records related to the user (user authorized only)
@records.route("/user/records/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_user_records():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get all the records related to the user from the database table
    record_list = Record.query \
        .join(Collection) \
        .filter(id==id, Collection.user_id==user_id) \
        .all()
    # Return an error if no records relate to the user in the datbase 
    if not record_list:
        return abort(401, description="No records related to this user")
    # Convert the records from the database into a JSON format and store them in result
    result = records_schema.dump(record_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a specific record created by a user
@records.route("/user/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_user_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
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


# The GET routes endpoint returning any records created by the user with a specifc album_title, or rpm
@records.route("/search", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def search_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
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


# The POST routes endpoint; any logged in user can post a new record to the database as long as they have a valid artist id, which they can search for 
# in the the GET routes endpoint for searching an artist by name. Collection table will be updated here as well.
@records.route("/", methods=["POST"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def create_record():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Load record data from the request, create a new Record object, and set its attributes
    record_fields = record_schema.load(request.json)
    new_record = Record()
    new_record.album_title = record_fields["album_title"]
    new_record.rpm = record_fields["rpm"]
    # Check if the artist_id exists in the Artist table
    if not Artist.query.get(record_fields["artist_id"]):
        return abort(400, description="Invalid artist_id")
    new_record.artist_id = record_fields["artist_id"]
    # Add to the database and commit record before committing collection, so that the collection has the record_id to add 
    db.session.add(new_record)
    db.session.commit()
    # Create a new Collection object, and set its attributes
    new_collection = Collection()
    new_collection.user_id = user_id
    new_collection.record_id = new_record.id
    # Add to the database and commit collection
    db.session.add(new_collection)
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(new_record))


# The PUT routes endpoint; authorized users who created the record can update the record data keeping record and artist id in tact 
@records.route("/<int:id>/", methods=["PUT"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def update_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the relationship between the record with the specified ID and the current user
    relationship = Record.query \
        .join(Collection) \
        .filter(Collection.record_id == id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized or the record does not exist
    if not relationship:
        return abort(401, description="Unauthorized user or record does not exist")
    # Get the record with the specified ID from the database
    record = Record.query.filter_by(id=id).first()
    # Load record data from the request, and update the attributes
    record_fields = record_schema.load(request.json)
    record.album_title = record_fields["album_title"]
    record.rpm = record_fields["rpm"]
    # Commit to the database
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(record))


# The DELETE routes endpoint; users who are authorized can delete records they have created
@records.route("/<int:id>/", methods=["DELETE"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def delete_record(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find the record in the db filtered by id, eagerly loading the related Artist object
    record = Record.query.options(joinedload(Record.artist)).filter_by(id=id).first()
    # Get the relationship between the record with the specified ID and the current user
    relationship = Record.query \
        .join(Collection) \
        .filter(Collection.record_id == id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized or the record does not exist
    if not relationship:
        return abort(401, description="Unauthorized user or record does not exist")
    # Delete the record from the database and commit
    db.session.delete(record)
    db.session.commit()
    # Return the record in the response
    return jsonify(record_schema.dump(record))
