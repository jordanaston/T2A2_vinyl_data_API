from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # creating our database object! This allows us to use our ORM
    db.init_app(app)

    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    # import the controllers and activate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app



