from flask import Blueprint, jsonify, request, abort
from main import db
from models.artists import Artist
from models.collections import Collection
from models.records import Record
from models.users import User
from schemas.artist_schema import artist_schema, artists_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import admin_required

# Create a Flask Blueprint for the /artists endpoint
artists = Blueprint('artists', __name__, url_prefix="/artists")

# The GET routes endpoint returning list of all artists in the database (admin authorized only)
@artists.route("/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_artists():
    # Get all the artists from the database table
    artist_list = Artist.query.all()
    # Convert the artists from the database into a JSON format and store them in the result
    result = artists_schema.dump(artist_list)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a single artist in the database (admin authorized only)
@artists.route("/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
# Check whether the user has admin permissions to access the endpoint
@admin_required
def get_artist(id):
    # Find the artist in the database by id
    artist = Artist.query.filter_by(id=id).first()
    # Stop the request if the artist does not exist
    if not artist:
        return abort(400, description= "Artist does not exist")
    # Convert the artist from the database into a JSON format and store them in result
    result = artist_schema.dump(artist)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning a list of all artists related to the user (user authorized only)
@artists.route("/user/artists/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_user_artists():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get all the artists related to the user from the database table
    artist_list = Artist.query \
        .join(Record) \
        .join(Collection) \
        .filter(Record.artist_id==Artist.id, Collection.user_id==user_id) \
        .all()
    # Return an error if no artists related to the user in the database 
    if not artist_list:
        return abort(401, description="No artists related to this user")
    # Convert the artists from the database into a JSON format and store them in result
    results = artists_schema.dump(artist_list)
    # Return the data in JSON format
    return jsonify(results)


# The GET routes endpoint returning a specific artist created by a user
@artists.route("/user/<int:id>/", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def get_user_artist(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the artist with the specified ID from the database
    artist = Artist.query.filter_by(id=id).first()
    # Return an error if the artist doesn't exist
    if not artist:
        return abort(400, description= "Artist does not exist")
    # Get the relationship between the artist with the specified ID and the current user
    relationship = Record.query \
        .join(Artist) \
        .join(Collection) \
        .filter(Artist.id == id, Collection.user_id == user_id, Collection.record_id == Record.id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Convert the artist from the database into a JSON format and store them in result
    result = artist_schema.dump(artist)
    # Return the data in JSON format
    return jsonify(result)


# The GET routes endpoint returning any artist created by the user filtered by artist name
@artists.route("/search", methods=["GET"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def search_tracks():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieve the value of the 'artist_name' parameter from the request
    artist_name = request.args.get('artist_name')
    # Query the database to retrieve a list of artists whose name matches the 'artist_name' parameter and 
    # whose records are associated with a collection belonging to the specified 'user_id'
    artist = Artist.query \
                .join(Record) \
                .join(Collection) \
                .filter(Artist.artist_name == artist_name, Collection.user_id == user_id) \
                .all()
    # Check if the artist searched for is in the user's collection, if not return a 400 error with a message.
    if not artist:
        return abort(400, description= "Artist not in your collection")
    # Convert the tracks from the database into a JSON format and store them in result
    result = artists_schema.dump(artist)
    # Return the data in JSON format
    return jsonify(result) 


# The POST route endpoint, any logged in user can post a new artist to the database
@artists.route("/", methods=["POST"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def create_artist():
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Load artist data from the request, create a new Artist object, and set its attributes
    artist_fields = artist_schema.load(request.json)
    new_artist = Artist()
    new_artist.artist_name = artist_fields["artist_name"]
    # Add to the database and commit
    db.session.add(new_artist)
    db.session.commit()
    # Return the artist in the response
    return jsonify(artist_schema.dump(new_artist))


# The PUT route endpoint, authorized users who created the artist can update the artist name keeping artist id in tact 
@artists.route("/<int:id>/", methods=["PUT"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def update_artist(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Get the artist with the specified ID from the database
    artist = Artist.query.filter_by(id=id).first()
    # Return an error if the artist doesn't exist
    if not Artist:
        return abort(400, description= "Artist does not exist")
    # Get the relationship between the artist with the specified ID and the current user
    relationship = Artist.query \
        .join(Record) \
        .join(Collection) \
        .filter(Artist.id==id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Load artist data from the request, and update the "artist_name" attribute
    artist_fields = artist_schema.load(request.json)
    artist.artist_name = artist_fields["artist_name"]
    # Commit to the database
    db.session.commit()
    # Return the artist in the response
    return jsonify(artist_schema.dump(artist))


# The DELETE route endpoint, users who are authorized can delete artists they have created 
@artists.route("/<int:id>/", methods=["DELETE"])
# Require a valid JWT token to access the endpoint
@jwt_required()
def delete_artist(id):
    # Get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Retrieves a user object from the database based on the provided user ID
    user = User.query.get(user_id)
    # Stop the request if the user is invalid
    if not user:
        return abort(401, description="Invalid user")
    # Get the relationship between the artist with the specified ID and the current user
    relationship = Artist.query \
        .join(Record) \
        .join(Collection) \
        .filter(Artist.id==id, Collection.user_id == user_id) \
        .first()
    # Stop the request if the user is unauthorized
    if not relationship:
        return abort(401, description="Unauthorized user")
    # Find the artist
    artist = Artist.query.filter_by(id=id).first()
    # Return an error if the artist doesn't exist
    if not Artist:
        return abort(400, description= "Artist doesn't exist")
    # Delete the artist from the database and commit
    db.session.delete(artist)
    db.session.commit()
    # Return the artist in the response
    return jsonify(artist_schema.dump(artist))