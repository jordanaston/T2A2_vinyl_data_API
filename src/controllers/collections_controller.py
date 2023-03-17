from flask import Blueprint, jsonify, abort
from models.collections import Collection
from schemas.collection_schema import collection_schema, collections_schema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import admin_required

# Create a Flask Blueprint for the /collections endpoint
collections = Blueprint('collections', __name__, url_prefix="/collections")

# The GET routes endpoint for a all collections (admin required)
@collections.route("/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_collections():
    # Query the database for all instances of the Collection model
    collection_list = Collection.query.all()
    # Serialize the collection data into JSON format 
    result = collections_schema.dump(collection_list)
    # Return the JSON data to the client as the HTTP response
    return jsonify(result)


# The GET routes endpoint for a single collection (admin required)
@collections.route("/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_collection(id):
    # Check if collection exists in database filtered by id
    collection = Collection.query.filter_by(id=id).first()
    # Return an error if the collection doesn't exist
    if not collection:
        return abort(400, description= "Collection does not exist")
    # Convert the collection from the database into a JSON format and store them in result
    result = collection_schema.dump(collection)
    # Return the data in JSON format
    return jsonify(result)



