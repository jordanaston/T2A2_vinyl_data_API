from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from datetime import date

users = Blueprint('users', __name__, url_prefix="/users")

# NEED TO ADD PUT REQUESTS FOR "UPDATE" CRUD FUNCTIONALITY

# The GET routes endpoint for getting list of all users
@users.route("/", methods=["GET"])
def get_users():
    # get all the users from the database table
    user_list = User.query.all()
    # Convert the cards from the database into a JSON format and store them in result
    result = users_schema.dump(user_list)
    # return the data in JSON format
    return jsonify(result)

# The GET routes endpoint for getting a single user
@users.route("/<int:id>/", methods=["GET"])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not user:
        return abort(400, description= "User does not exist")
    # Convert the cards from the database into a JSON format and store them in result
    result = user_schema.dump(user)
    # return the data in JSON format
    return jsonify(result)

# The POST route endpoint
@users.route("/", methods=["POST"])
def create_user():
    # #Create a new card
    user_fields = user_schema.load(request.json)

    new_user = User()
    new_user.user_name = user_fields["user_name"]
    new_user.email = user_fields["email"]
    new_user.password = user_fields["password"]
    new_user.admin = user_fields["admin"]
    
    # add to the database and commit
    db.session.add(new_user)
    db.session.commit()
    # #return the card in the response
    return jsonify(user_schema.dump(new_user))


# Finally, we round out our CRUD resource with a DELETE method
@users.route("/<int:id>/", methods=["DELETE"])
def delete_user(id):
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
    user = User.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not User:
        return abort(400, description= "User doesn't exist")
    #Delete the card from the database and commit
    db.session.delete(user)
    db.session.commit()
    #return the card in the response
    return jsonify(user_schema.dump(user))