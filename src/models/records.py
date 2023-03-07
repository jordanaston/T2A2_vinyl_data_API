from main import db

class Record(db.Model):
    # define the table name for the db
    __tablename__= "RECORDS"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    album_title = db.Column(db.String())
    rpm = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    