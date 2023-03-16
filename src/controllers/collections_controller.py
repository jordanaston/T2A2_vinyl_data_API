from flask import Blueprint, jsonify, abort
from models.collections import Collection
from models.users import User
from schemas.collection_schema import collection_schema, collections_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps

# Create a Flask Blueprint for the /collections endpoint
collections = Blueprint('collections', __name__, url_prefix="/collections")

# Utilize a decorator for checking if a user is an admin to reduce repetitive code
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user.admin:
            abort(401, description="Unauthorized user")
        return fn(*args, **kwargs)
    return wrapper


@collections.route("/", methods=["GET"])
@jwt_required()
@admin_required
def get_collections():
    collection_list = Collection.query.all()
    result = collections_schema.dump(collection_list)
    return jsonify(result)


# The GET routes endpoint for a single collection (admin required)
@collections.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_collection(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Check if collection exists in database filtered by id
    collection = Collection.query.filter_by(id=id).first()
    # Return an error if the collection doesn't exist
    if not collection:
        return abort(400, description= "Collection does not exist")
    # Convert the collection from the database into a JSON format and store them in result
    result = collection_schema.dump(collection)
    # Return the data in JSON format
    return jsonify(result)



