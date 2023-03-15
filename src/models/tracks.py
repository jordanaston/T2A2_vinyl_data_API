from main import db

class Track(db.Model):
    # Define the table name for the db
    __tablename__= "tracks"
    # Set the primary key, and field properties
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # Add the rest of the attributes. 
    track_title = db.Column(db.String(), nullable=False)
    bpm = db.Column(db.Integer())
    key = db.Column(db.String())
    record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)