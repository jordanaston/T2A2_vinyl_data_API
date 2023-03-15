from main import db
from flask import Blueprint
from main import bcrypt
from models.users import User
from models.records import Record
from models.collections import Collection
from models.artists import Artist
from models.tracks import Track

# Defines a Flask Blueprint that provides database-related commands
db_commands = Blueprint("db", __name__)

# Creates the app's cli command named create, invoking create_db function
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

# Creates the app's cli command named seed, invoking seed_db function
@db_commands.cli.command("seed")
def seed_db():

    # Creates a User instance for admin, named with the specified attributes
    admin_user = User(
        user_name = "admin_user",
        email = "admin@email.com",
        # The password is hashed using the bcrypt library to securely store it.
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    # Add the object as a new row to the table
    db.session.add(admin_user)

    # Creates a User instance named with the specified attributes
    user1 = User(
        user_name = "user_1",
        email = "user1@email.com",
        # The password is hashed using the bcrypt library to securely store it.
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = False
    )
    # Add the object as a new row to the table
    db.session.add(user1)

    # Creates a User instance named with the specified attributes
    user2 = User(
        user_name = "user_2",
        email = "user2@email.com",
        # The password is hashed using the bcrypt library to securely store it.
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = False
    )
    # Add the object as a new row to the table
    db.session.add(user2)

    # This extra commit will end the transaction and generate the ids for the users
    db.session.commit()

    # Creates an Artist instance named with the specified attributes
    artist1 = Artist(
        artist_name = "Aphex Twin",
    )
    # Add the object as a new row to the table
    db.session.add(artist1)

    # Creates an Artist instance named with the specified attributes
    artist2 = Artist(
        artist_name = "Chaos In The CBD",
    )
    # Add the object as a new row to the table
    db.session.add(artist2)

    # Creates an Artist instance named with the specified attributes
    artist3 = Artist(
        artist_name = "Jimmy Whoo",
    )
    # Add the object as a new row to the table
    db.session.add(artist3)

    # This extra commit will end the transaction and generate the ids for the artists
    db.session.commit()

    # Creates a Record instance named with the specified attributes
    record1 = Record(
        album_title = "Selected Ambient Works 85-92",
        rpm = 33,
        artist_id = artist1.id
    )
    # Add the object as a new row to the table
    db.session.add(record1)

    # Creates a Record instance named with the specified attributes
    record2 = Record(
        album_title = "Intimate Fantasy - EP",
        rpm = 45,
        artist_id = artist2.id
    )
    # Add the object as a new row to the table
    db.session.add(record2)

    # Creates a Record instance named with the specified attributes
    record3 = Record(
        album_title = "Motel Music Part 3",
        rpm = 45,
        artist_id = artist3.id
    )
    # Add the object as a new row to the table
    db.session.add(record3)

    # This extra commit will end the transaction and generate the ids for the records
    db.session.commit()

    # Creates a Collection instance named with the specified attributes
    collection1 = Collection(
        user_id = user1.id,
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(collection1)

    # Creates a Collection instance named with the specified attributes
    collection2 = Collection(
        user_id = user2.id,
        record_id = record2.id
    )
    # Add the object as a new row to the table
    db.session.add(collection2)

    # Creates a Collection instance named with the specified attributes
    collection3 = Collection(
        user_id = user2.id,
        record_id = record3.id
    )
    # Add the object as a new row to the table
    db.session.add(collection3)

    # Creates a Collection instance named with the specified attributes
    track1 = Track(
        # Set the attributes
        track_title = "Xtal",
        bpm = 115,
        key = "A# Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track1)

    # Creates a Collection instance named with the specified attributes
    track2 = Track(
        # Set the attributes
        track_title = "Delphium",
        bpm = 135,
        key = "E Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track2)

    # Creates a Collection instance named with the specified attributes
    track3 = Track(
        # Set the attributes
        track_title = "Pulsewidth",
        bpm = 119,
        key = "C# Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track3)

    # Creates a Collection instance named with the specified attributes
    track4 = Track(
        # Set the attributes
        track_title = "Ageispolis",
        bpm = 102,
        key = "F# Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track4)

    # Creates a Collection instance named with the specified attributes
    track5 = Track(
        # Set the attributes
        track_title = "Green Calx",
        bpm = 117,
        key = "G Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track5)

    # Creates a Collection instance named with the specified attributes
    track6 = Track(
        # Set the attributes
        track_title = "Heliosphan",
        bpm = 131,
        key = "C Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track6)

    # Creates a Collection instance named with the specified attributes
    track7 = Track(
        # Set the attributes
        track_title = "Ptolemy",
        bpm = 102,
        key = "E Minor",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track7)

    # Creates a Collection instance named with the specified attributes
    track7 = Track(
        # Set the attributes
        track_title = "Actium",
        bpm = 135,
        key = "A# Major",
        record_id = record1.id
    )
    # Add the object as a new row to the table
    db.session.add(track7)

    # Creates a Collection instance named with the specified attributes
    track8 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Club Miyako",
        bpm = 131,
        key = "C Minor",
        record_id = record2.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track8)

    # Creates a Collection instance named with the specified attributes
    track9 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Intimate Fantasy",
        bpm = 79,
        key = "D Minor",
        record_id = record2.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track9)

    # Creates a Collection instance named with the specified attributes
    track10 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Intro Ciel Rouge",
        bpm = 120,
        key = "E Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track10)

    # Creates a Collection instance named with the specified attributes
    track11 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Devil In my Heart",
        bpm = 120,
        key = "G Major",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track11)

    # Creates a Collection instance named with the specified attributes
    track12 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Ain't The Same",
        bpm = 135,
        key = "F# Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track12)

    # Creates a Collection instance named with the specified attributes
    track13 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Bingo Bongo",
        bpm = 119,
        key = "C# Major",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track13)

    # Creates a Collection instance named with the specified attributes
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

    # Creates a Collection instance named with the specified attributes
    track16 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Satin Dolls",
        bpm = 79,
        key = "F Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track16)

    # Creates a Collection instance named with the specified attributes
    track16 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Aqua",
        bpm = 102,
        key = "Bb Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track16)

    # Creates a Collection instance named with the specified attributes
    track17 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Waves",
        bpm = 117,
        key = "Bb Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track17)
    
    # Creates a Collection instance named with the specified attributes
    track18 = Track(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        track_title = "Chapel Of Love",
        bpm = 120,
        key = "D Minor",
        record_id = record3.id
    )
    # Add the object as a new row to the tablef
    db.session.add(track18)

    # Commit the changes
    db.session.commit()
    print("Table seeded") 

# Creates the app's cli command named drop, invoking drop_db function
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")