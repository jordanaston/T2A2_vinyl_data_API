from main import db

class Track(db.Model):
    # define the table name for the db
    __tablename__= "TRACKS"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    track_title = db.Column(db.String())
    bpm = db.Column(db.Integer())
    key = db.Column(db.String())
    record_id = db.Column(db.Integer, db.ForeignKey('RECORDS.id'))