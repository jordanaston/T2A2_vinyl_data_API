from main import db

class Record(db.Model):
    # Define the table name for the db
    __tablename__= "records"
    # Set the primary key, and field properties
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # Add the rest of the attributes. 
    album_title = db.Column(db.String(), nullable=False)
    rpm = db.Column(db.Integer())
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    # Creates a one-to-many relationship between the Record and Collection tables in the database.
    # when an record is deleted, all their associated records will also be deleted (due to the "cascade" parameter).
    collections = db.relationship(
        "Collection",
        backref="record",
        cascade="all, delete"
    )
    # Creates a one-to-many relationship between the Record and Track tables in the database.
    # when an record is deleted, all their associated records will also be deleted (due to the "cascade" parameter).
    tracks = db.relationship(
        "Track",
        backref="record",
        cascade="all, delete"
    )
    