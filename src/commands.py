from main import db
from flask import Blueprint
from main import bcrypt
from models.users import User
from models.records import Record
from models.collections import Collection
from models.artists import Artist
from models.tracks import Track
from datetime import date

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask create", 
# it will invoke create_db function
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

# @db_commands.cli.command("seed")
# def seed_db():
#     # create the card object
#     card1 = Card(
#         # set the attributes, not the id, SQLAlchemy will manage that for us
#         title = "Start the project",
#         description = "Stage 1, creating the database",
#         status = "To Do",
#         priority = "High",
#         date = date.today()
#     )
#     # Add the object as a new row to the table
#     db.session.add(card1)

#     card2 = Card(
#         # set the attributes, not the id, SQLAlchemy will manage that for us
#         title = "SQLAlchemy and Marshmallow",
#         description = "Stage 2, integrate both modules in the project",
#         status = "Ongoing",
#         priority = "High",
#         date = date.today()
#     )
#     # Add the object as a new row to the tablef
#     db.session.add(card2)


#     admin_user = User(
#         email = "admin@email.com",
#         password = bcrypt.generate_password_hash("password123").decode("utf-8"),
#         admin = True
#     )
#     db.session.add(admin_user)

#     user1 = User(
#         email = "user1@email.com",
#         password = bcrypt.generate_password_hash("123456").decode("utf-8")
#     )
#     db.session.add(user1)
#     # commit the changes
#     db.session.commit()
#     print("Table seeded") 

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 