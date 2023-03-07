from main import db

class User(db.Model):
    # define the table name for the db
    __tablename__= "USERS"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    user_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())