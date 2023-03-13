from main import db

class Artist(db.Model):
    # define the table name for the db
    __tablename__= "artists"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # Add the rest of the attributes. 
    artist_name = db.Column(db.String(), nullable=False)

    records = db.relationship(
        "Record",
        backref="artist",
        cascade="all, delete"
    )