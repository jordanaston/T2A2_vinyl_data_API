from main import ma
from marshmallow.validate import Length, Range
from marshmallow import fields, pre_load
import html

# Record Schema created with Marshmallow, providing serialization needed for converting the data into JSON
class RecordSchema(ma.Schema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Fields to expose
        fields = ("id", "album_title", "rpm", "artist_id", "artist")
    # Schema nesting: adds artist_name to the response 
    artist = fields.Nested("ArtistSchema", only=("artist_name",))
    # Add length validation for album_title 
    album_title = ma.String(validate=Length(min=1, max=100))
    # Add range validation for rpm 
    rpm = ma.Integer(validate=Range(min=1, max=120))

    # Sanitization function to escape special characters in album_title
    @pre_load
    def sanitize_album_title(self, data, **kwargs):
        if "album_title" in data:
            data["album_title"] = html.escape(data["album_title"].strip())
        return data
    
# Single record schema, when one record needs to be retrieved
record_schema = RecordSchema()
# Multiple records schema, when many records need to be retrieved
records_schema = RecordSchema(many=True)

