from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from main import bcrypt

# Create a Flask Blueprint for the /users endpoint
users = Blueprint('users', __name__, url_prefix="/users")

# The GET route endpoint for getting list of all users (admin required)
@users.route("/", methods=["GET"])
@jwt_required()
def get_users():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Get all the users from the database table
    user_list = User.query.all()
    # Convert the users from the database into a JSON format and store them in result
    result = users_schema.dump(user_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint for getting a single user (admin required)
@users.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_user(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Query database for user
    user_in_db = User.query.filter_by(id=id).first()
    # Return an error if the user doesn't exist
    if not user_in_db:
        return abort(400, description= "User does not exist")
    # Convert the user from the database into a JSON format and store them in result
    result = user_schema.dump(user_in_db)
    # return the data in JSON format
    return jsonify(result)


# The POST route endpoint for creating a new user (admin required)
@users.route("/", methods=["POST"])
@jwt_required()
def create_user():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorized user")
    # Create a new user
    user_fields = user_schema.load(request.json)
    new_user = User()
    new_user.user_name = user_fields["user_name"]
    new_user.email = user_fields["email"]
    new_user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8"),
    # Admin chooses if admin=true or false
    new_user.admin = user_fields["admin"]
    # Add to the database and commit
    db.session.add(new_user)
    db.session.commit()
    # Return the user in the response
    return jsonify(user_schema.dump(new_user))


# The PUT route endpoint granting users permission to update their user fields (except admin field). 
@users.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_user(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find the user in the db based on their ID
    user = User.query.filter_by(id=user_id).first()
    # Stop request if user invalid
    if not user:
        return abort(401, description="Invalid user")
    # Only allow users to update their own fields
    if user.id != id:
        return abort(401, description="You are not authorized to update this user")
    # Create a new user
    user_fields = user_schema.load(request.json)
    # Update the user details with the given values
    user.user_name = user_fields["user_name"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    # User not allowed to set admin to True
    user.admin = False
    # Add to the database and commit
    db.session.commit()
    # Return the updated user in the response
    return jsonify(user_schema.dump(user))


# The DELETE routes endpoint, allowing only admin to delete users
@users.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="You are not authorized to delete users")
    # Find the user
    find_user = User.query.filter_by(id=id).first()
    # Return an error if the user doesn't exist
    if not find_user:
        return abort(400, description= "User does not exist")
    # Delete the user from the database and commit
    db.session.delete(find_user)
    db.session.commit()
    # Return the user in the response
    return jsonify(user_schema.dump(find_user))

