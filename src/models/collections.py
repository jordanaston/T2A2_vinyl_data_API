from main import db

class Collection(db.Model):
    # Define the table name for the db
    __tablename__= "collections"
    # Set the primary key, and field properties
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # Add the rest of the attributes.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)