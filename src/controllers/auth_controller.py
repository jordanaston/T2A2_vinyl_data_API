# from flask import Blueprint, jsonify, request, abort
# from main import db
# from models.users import User
# from schemas.user_schema import user_schema, users_schema
# from datetime import timedelta
# from main import bcrypt
# from flask_jwt_extended import create_access_token

# auth = Blueprint('auth', __name__, url_prefix="/auth")

# @auth.route("/register", methods=["POST"])
# def auth_register():
#     #The request data will be loaded in a user_schema converted to JSON. request needs to be imported from
#     user_fields = user_schema.load(request.json)
#     # find the user
#     user = User.query.filter_by(email=user_fields["email"]).first()

#     if user:
#         # return an abort message to inform the user. That will end the request
#         return abort(400, description="Email already registered")
#     # Create the user object
#     user = User()
#     #Add the email attribute
#     user.email = user_fields["email"]
#     #Add the password attribute hashed by bcrypt
#     user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
#     #set the admin attribute to false
#     user.admin = False
#     #Add it to the database and commit the changes
#     db.session.add(user)
#     db.session.commit()
#     #create a variable that sets an expiry date
#     expiry = timedelta(days=1)
#     #create the access token
#     access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
#     # return the user email and the access token
#     return jsonify({"user":user.email, "token": access_token })


# @auth.route("/login", methods=["POST"])
# def auth_login():
#     # get the user data from the request
#     user_fields = user_schema.load(request.json)
#     #find the user in the database by email
#     user = User.query.filter_by(email=user_fields["email"]).first()
#     # there is not a user with that email or if the password is no correct send an error
#     if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
#         return abort(401, description="Incorrect username and password")
    
#     #create a variable that sets an expiry date
#     expiry = timedelta(days=1)
#     #create the access token
#     access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
#     # return the user email and the access token
#     return jsonify({"user":user.email, "token": access_token })