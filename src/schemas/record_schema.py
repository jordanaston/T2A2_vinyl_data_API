from main import ma
from marshmallow import fields

# Record Schema created with Marshmallow, providing serialization needed for converting the data into JSON
class RecordSchema(ma.Schema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Fields to expose
        fields = ("id", "album_title", "rpm", "artist_id", "artist")
    # Schema nesting: adds artist_name to the response 
    artist = fields.Nested("ArtistSchema", only=("artist_name",))

# Single record schema, when one record needs to be retrieved
record_schema = RecordSchema()
# Multiple records schema, when many records need to be retrieved
records_schema = RecordSchema(many=True)

