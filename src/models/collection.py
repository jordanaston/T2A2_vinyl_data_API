from main import db

class Collection(db.Model):
    # define the table name for the db
    __tablename__= "COLLECTIONS"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'))

    record_id = db.Column(db.Integer, db.ForeignKey('RECORDS.id'))