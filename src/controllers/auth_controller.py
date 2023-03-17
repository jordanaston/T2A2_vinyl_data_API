from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema
from datetime import timedelta
from main import bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from functools import wraps

# Create a Flask Blueprint for the /auth endpoint
auth = Blueprint('auth', __name__, url_prefix="/auth")

# POST routes endpoint for registering a new user who's email is not already registered
@auth.route("/register", methods=["POST"])
def auth_register():
    # The request data loaded in a user_schema 
    user_fields = user_schema.load(request.json)
    # Query the User table for the first user with the given email address
    user = User.query.filter_by(email=user_fields["email"]).first()
    # Return an abort message to inform the user is already registered. 
    if user:
        return abort(400, description="Email already registered")
    # Create the user object
    user = User()
    # Add the attributes
    user.user_name = user_fields["user_name"]
    user.email = user_fields["email"]
    # Add the password attribute hashed by bcrypt
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    # Set the admin attribute to false as user will not be admin
    user.admin = False
    # Add it to the database and commit the changes
    db.session.add(user)
    db.session.commit()
    # Set an expiry date
    expiry = timedelta(days=1)
    # Create the access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # Return the user email and the access token
    return jsonify({"user":user.email, "token": access_token })

# POST routes endpoint for logging in an existing user, generating an access token
@auth.route("/login", methods=["POST"])
def auth_login():
    # Get the user data from the request
    user_fields = user_schema.load(request.json)
    # Query the User table for the first user with the given email address
    user = User.query.filter_by(email=user_fields["email"]).first()
    # If there is no user with that email or if the password isn't correct send an error
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")
    # Set an expiry date
    expiry = timedelta(days=1)
    # Create the access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # Return the user email and the access token
    return jsonify({"user":user.email, "token": access_token })


# Utilize a decorator in other controllers for checking if a user is an admin to reduce repetitive code
def admin_required(fn):
     # Use the functools.wraps decorator to preserve the original function name and signature
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Get the user id invoking get_jwt_identity
        user_id = get_jwt_identity()
        # Retrieves a user object from the database based on the provided user ID
        user = User.query.get(user_id)
        # Stop the request if the user is not an admin
        if not user.admin:
            abort(401, description="Unauthorized user")
        return fn(*args, **kwargs)
    # Return the wrapped function
    return wrapper