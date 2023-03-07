from main import ma
from marshmallow.validate import Length
from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    #set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)