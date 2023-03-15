from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Instantiate SQLAlchemy object for object-relational mapping
db = SQLAlchemy()
# Instantiate Marshmallow object for object serialization and deserialization
ma = Marshmallow()
# Instantiate Bcrypt object for password hashing and verification
bcrypt = Bcrypt()
# Instantiate JWTManager object for JSON Web Token (JWT) handling
jwt = JWTManager()

def create_app():
    # Create the flask app object
    app = Flask(__name__)
    # Congfigure the app
    app.config.from_object("config.app_config")
    # Create the database object allowing for ORM use
    db.init_app(app)
    # Initialize the Marshmallow object with the Flask app instance
    ma.init_app(app)
    # Create the jwt and bcrypt objects allowing for authentication
    bcrypt.init_app(app)
    jwt.init_app(app)
    # Import and register the database-related command blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)
    # Imports the controllers and activate the blueprints
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    return app



