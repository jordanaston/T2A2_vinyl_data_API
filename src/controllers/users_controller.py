from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from main import bcrypt
from controllers.auth_controller import admin_required

# Create a Flask Blueprint for the /users endpoint
users = Blueprint('users', __name__, url_prefix="/users")

# The GET route endpoint for getting list of all users (admin required)
@users.route("/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_users():
    # Get all the users from the database table
    user_list = User.query.all()
    # Convert the users from the database into a JSON format and store them in result
    result = users_schema.dump(user_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint for getting a single user (admin required)
@users.route("/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_user(id):
    # Query database for user filtering by id
    user_in_db = User.query.filter_by(id=id).first()
    # Return an error if the user doesn't exist
    if not user_in_db:
        return abort(400, description= "User does not exist")
    # Convert the user from the database into a JSON format and store them in result
    result = user_schema.dump(user_in_db)
    # return the data in JSON format
    return jsonify(result)


# The POST routes endpoint for creating a new user (admin required)
@users.route("/", methods=["POST"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def create_user():
    # Load user data from the request
    user_fields = user_schema.load(request.json)
    # Try to extract the required fields and catch KeyError if any field is missing
    try:
        user_name = user_fields["user_name"]
        email = user_fields["email"]
        password = user_fields["password"]
        admin = user_fields["admin"]
    except KeyError:
        return abort(400, description="Missing data for required fields")
    # Check if a user with the same email already exists in the database
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return abort(409, description="User with that email already exists")
    # Create a new User object, and set its attributes
    new_user = User()
    new_user.user_name = user_name
    new_user.email = email
    new_user.password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user.admin = admin
    # Add to the database and commit
    db.session.add(new_user)
    db.session.commit()
    # Return the user in the response
    return jsonify(user_schema.dump(new_user))


# The PUT routes endpoint granting users permission to update their user fields (except admin field). 
@users.route("/<int:id>/", methods=["PUT"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def update_user(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find the user in the db based on their ID
    user = User.query.filter_by(id=user_id).first()
    # Only allow users to update their own fields
    if user.id != id:
        return abort(401, description="You are not authorized to update this user")
    # Load user data from the request
    user_fields = user_schema.load(request.json)
    # Try to extract the required fields and catch KeyError if any field is missing
    try:
        user_name = user_fields["user_name"]
        email = user_fields["email"]
        password = user_fields["password"]
    except KeyError:
        return abort(400, description="Missing data for required fields")
    # Set the user attributes
    user.user_name = user_name
    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")
    # User not allowed to set admin to True
    user.admin = False
    # Add to the database and commit
    db.session.commit()
    # Return the updated user in the response
    return jsonify(user_schema.dump(user))


# The DELETE routes endpoint; allowing only admin to delete users
@users.route("/<int:id>/", methods=["DELETE"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def delete_user(id):
    # Find the user in the database filtering by ID
    find_user = User.query.filter_by(id=id).first()
    # Return an error if the user doesn't exist
    if not find_user:
        return abort(400, description= "User does not exist")
    # Delete the user from the database and commit
    db.session.delete(find_user)
    db.session.commit()
    # Return the user in the response
    return jsonify(user_schema.dump(find_user))


