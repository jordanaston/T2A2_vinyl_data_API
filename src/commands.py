from main import db
from flask import Blueprint
from main import bcrypt
from models.users import User
from models.records import Record
from models.collections import Collection
from models.artists import Artist
from models.tracks import Track
from datetime import date

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask create", 
# it will invoke create_db function
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("seed")
def seed_db():

    admin_user = User(
        user_name = "admin_user",
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    # Add the object as a new row to the table
    db.session.add(admin_user)

    user1 = User(
        user_name = "user_1",
        email = "user1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = False
    )
    # Add the object as a new row to the table
    db.session.add(user1)

    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    # create the card object
    record1 = Record(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        album_title = "Selected Ambient Works 85-92",
        rpm = 33,
        user_id = user1.id
    )
    # Add the object as a new row to the table
    db.session.add(record1)

    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    collection1 = Collection(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        user_id = user1.id,
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(collection1)

    artist1 = Artist(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        artist_name = "Aphex Twin",
        record_id = record1.id
    )
    # Add the object as a new row to the tablef
    db.session.add(artist1)

    track1 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Heliosphan",
        bpm = 131,
        key = "C Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track1)

    # commit the changes
    db.session.commit()
    print("Table seeded") 


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 