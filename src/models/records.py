from main import db

class Record(db.Model):
    # define the table name for the db
    __tablename__= "records"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # Add the rest of the attributes. 
    album_title = db.Column(db.String(), nullable=False)
    rpm = db.Column(db.Integer())
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    
    collections = db.relationship(
        "Collection",
        backref="record",
        cascade="all, delete"
    )
    tracks = db.relationship(
        "Track",
        backref="record",
        cascade="all, delete"
    )
    