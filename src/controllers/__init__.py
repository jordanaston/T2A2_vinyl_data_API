from controllers.users_controller import users
from controllers.records_controller import records 
from controllers.collections_controller import collections
from controllers.artists_controller import artists
from controllers.tracks_controller import tracks
from controllers.auth_controller import auth

# List of registerable controllers containing endpoints for the various resources
registerable_controllers = [
    auth,
    users,
    records,
    collections,
    artists,
    tracks
]