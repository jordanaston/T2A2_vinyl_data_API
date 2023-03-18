from main import db

class Artist(db.Model):
    # Define the table name for the db
    __tablename__= "artists"
    # Set the primary key, and field properties
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # Add the rest of the attributes. 
    artist_name = db.Column(db.String(), nullable=False, unique=True)
    # Creates a one-to-many relationship between the Artist and Record tables in the database.
    # when an artist is deleted, all their associated records will also be deleted (due to the "cascade" parameter).
    records = db.relationship(
        "Record",
        backref="artist",
        cascade="all, delete"
    )