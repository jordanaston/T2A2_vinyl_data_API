from main import ma
from marshmallow.validate import Length, Email
from models.users import User
from marshmallow import fields, pre_load
import html

# Defines a schema for the User model using the SQLAlchemyAutoSchema class.
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Specifies that the User model will be used to generate the schema.
        model = User
        # Fields to expose
        fields = ("id", "user_name", "email", "password", "admin")
    # Add length validation for user_name (assuming minimum 3 and maximum 50 characters)
    user_name = ma.String(validate=Length(min=3, max=50))
    # Add email format validation
    email = ma.String(validate=Email())
    # Set the password's length to a minimum of 6 characters and maximum of 50
    password = ma.String(validate=Length(min=6, max=50))
    # Add boolean validation for the admin field
    admin = fields.Boolean()

     # Sanitization function to escape special characters in user_name and email
    @pre_load
    def sanitize_fields(self, data, **kwargs):
        if "user_name" in data:
            data["user_name"] = html.escape(data["user_name"].strip())
        if "email" in data:
            data["email"] = html.escape(data["email"].strip())
        return data
    
# Single user schema, when one user needs to be retrieved
user_schema = UserSchema()
# Multiple users schema, when many users needs to be retrieved
users_schema = UserSchema(many=True)