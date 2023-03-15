from main import db
from flask import Blueprint
from main import bcrypt
from models.users import User
from models.records import Record
from models.collections import Collection
from models.artists import Artist
from models.tracks import Track

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

    user2 = User(
        user_name = "user_2",
        email = "user2@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = False
    )
    # Add the object as a new row to the table
    db.session.add(user2)

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

    artist3 = Artist(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        artist_name = "Jimmy Whoo",
    )
    # Add the object as a new row to the tablef
    db.session.add(artist3)

    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    # create the card object
    record1 = Record(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        album_title = "Selected Ambient Works 85-92",
        rpm = 33,
        artist_id = artist1.id
    )
    # Add the object as a new row to the table
    db.session.add(record1)

    # create the card object
    record2 = Record(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        album_title = "Intimate Fantasy - EP",
        rpm = 45,
        artist_id = artist2.id
    )
    # Add the object as a new row to the table
    db.session.add(record2)

    record3 = Record(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        album_title = "Motel Music Part 3",
        rpm = 45,
        artist_id = artist3.id
    )
    # Add the object as a new row to the table
    db.session.add(record3)

    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    collection1 = Collection(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        user_id = user1.id,
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(collection1)

    collection2 = Collection(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        user_id = user2.id,
        record_id = record2.id
    )
    # Add the object as a new row to the table
    db.session.add(collection2)

    collection3 = Collection(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        user_id = user2.id,
        record_id = record3.id
    )
    # Add the object as a new row to the table
    db.session.add(collection3)

    track1 = Track(
        # Set the attributes
        track_title = "Xtal",
        bpm = 115,
        key = "A# Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track1)

    track2 = Track(
        # Set the attributes
        track_title = "Delphium",
        bpm = 135,
        key = "E Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track2)

    track3 = Track(
        # Set the attributes
        track_title = "Pulsewidth",
        bpm = 119,
        key = "C# Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track3)

    track4 = Track(
        # Set the attributes
        track_title = "Ageispolis",
        bpm = 102,
        key = "F# Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track4)

    track5 = Track(
        # Set the attributes
        track_title = "Green Calx",
        bpm = 117,
        key = "G Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track5)

    track6 = Track(
        # Set the attributes
        track_title = "Heliosphan",
        bpm = 131,
        key = "C Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track6)

    track7 = Track(
        # Set the attributes
        track_title = "Ptolemy",
        bpm = 102,
        key = "E Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track7)

    track7 = Track(
        # Set the attributes
        track_title = "Actium",
        bpm = 135,
        key = "A# Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track7)

    track8 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Club Miyako",
        bpm = 131,
        key = "C Minor",
        record_id = record2.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track8)

    track9 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Intimate Fantasy",
        bpm = 79,
        key = "D Minor",
        record_id = record2.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track9)

    track10 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Intro Ciel Rouge",
        bpm = 120,
        key = "E Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track10)

    track11 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Devil In my Heart",
        bpm = 120,
        key = "G Major",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track11)

    track12 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Ain't The Same",
        bpm = 135,
        key = "F# Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track12)

    track13 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Bingo Bongo",
        bpm = 119,
        key = "C# Major",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track13)

    track14 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Perfect World",
        bpm = 115,
        key = "D Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track14)

    track15 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Get With Me",
        bpm = 131,
        key = "F Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track15)

    track16 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Satin Dolls",
        bpm = 79,
        key = "F Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track16)

    track16 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Aqua",
        bpm = 102,
        key = "Bb Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track16)

    track17 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Waves",
        bpm = 117,
        key = "Bb Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track17)

    track18 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Chapel Of Love",
        bpm = 120,
        key = "D Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track18)

    # commit the changes
    db.session.commit()
    print("Table seeded") 

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")