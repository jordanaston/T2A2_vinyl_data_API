from main import ma
from marshmallow.validate import Length
from models.users import User

# Defines a schema for the User model using the SQLAlchemyAutoSchema class.
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Specifies that the User model will be used to generate the schema.
        model = User
        # Fields to expose
        fields = ("id", "user_name", "email", "password", "admin")
    # Set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))

# Single user schema, when one user needs to be retrieved
user_schema = UserSchema()
# Multiple users schema, when many users needs to be retrieved
users_schema = UserSchema(many=True)