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

    test_user = User(
        user_name = "test_user",
        email = "test_user@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = False
    )
    # Add the object as a new row to the table
    db.session.add(test_user)

    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    artist1 = Artist(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        artist_name = "Aphex Twin",
    )
    # Add the object as a new row to the tablef
    db.session.add(artist1)

    artist2 = Artist(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        artist_name = "Chaos In The CBD",
    )
    # Add the object as a new row to the tablef
    db.session.add(artist2)

    # create the card object
    record1 = Record(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        album_title = "Selected Ambient Works 85-92",
        rpm = 33,
        user_id = test_user.id,
        artist_id = artist1.id
    )
    # Add the object as a new row to the table
    db.session.add(record1)

    # create the card object
    record2 = Record(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        album_title = "Intimate Fantasy - EP",
        rpm = 45,
        user_id = test_user.id,
        artist_id = artist2.id
    )
    # Add the object as a new row to the table
    db.session.add(record2)

    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    collection1 = Collection(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        user_id = test_user.id,
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(collection1)

    collection2 = Collection(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        user_id = test_user.id,
        record_id = record2.id
    )
    # Add the object as a new row to the table
    db.session.add(collection2)

    track1 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Heliosphan",
        bpm = 126,
        key = "E Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track1)

    track2 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Club Miyako",
        bpm = 131,
        key = "C Minor",
        record_id = record2.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track2)

    # commit the changes
    db.session.commit()
    print("Table seeded") 


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 