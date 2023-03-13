from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from main import bcrypt

users = Blueprint('users', __name__, url_prefix="/users")


# WORKING WORKING WORKING

# The GET routes endpoint for getting list of all users
@users.route("/", methods=["GET"])
@jwt_required()
def get_users():
    user_id = get_jwt_identity()
    
    # get all the users from the database table
    user_list = User.query.all()

    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    
    # Convert the cards from the database into a JSON format and store them in result
    result = users_schema.dump(user_list)
    # return the data in JSON format
    return jsonify(result)


# WORKING WORKING WORKING

# The GET routes endpoint for getting a single user
@users.route("/<int:id>/", methods=["GET"])
@jwt_required()
def get_user(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    
    user = User.query.filter_by(id=id).first()
    # Return an error if the user doesn't exist
    if not user:
        return abort(400, description= "User does not exist")
    
    # Find it in the db
    auth_user = User.query.get(user_id)
    # Make sure it is in the database
    if user != auth_user:
        return abort(401, description="Invalid user")
    # Convert the user from the database into a JSON format and store them in result
    result = user_schema.dump(user)
    # return the data in JSON format
    return jsonify(result)


# WORKING WORKING WORKING

# The POST route endpoint
@users.route("/", methods=["POST"])
@jwt_required()
def create_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # Create a new user
    user_fields = user_schema.load(request.json)

    new_user = User()
    new_user.user_name = user_fields["user_name"]
    new_user.email = user_fields["email"]
    new_user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8"),
    new_user.admin = user_fields["admin"]
    
    # add to the database and commit
    db.session.add(new_user)
    db.session.commit()
    # #return the card in the response
    return jsonify(user_schema.dump(new_user))

# WORKING WORKING WORKING

# The PUT route endpoint
@users.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_user(id):

    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()

    # Create a new user
    user_fields = user_schema.load(request.json)

    # find the user
    user = User.query.filter_by(id=id).first()
    #return an error if the user doesn't exist
    if not user:
        return abort(400, description= "User does not exist")
    
    # Find it in the db
    auth_user = User.query.get(user_id)
    # Make sure it is in the database
    if user != auth_user:
        return abort(401, description="Invalid user")
    
    #update the user details with the given values
    user.user_name = user_fields["user_name"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    user.admin = False
    
    # add to the database and commit
    db.session.commit()
    #return the card in the response
    return jsonify(user_schema.dump(user))

# WORKING WORKING WORKING

# Finally, we round out our CRUD resource with a DELETE method
@users.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
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

# Users cannot delete any users (including themselves), only admins can. This code is working exactly like this 