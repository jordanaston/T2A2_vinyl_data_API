from main import ma
from marshmallow import fields

# Create the Track Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class TrackSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "track_title", "bpm", "key", "record_id", "record")
    record = fields.Nested("RecordSchema", only=("album_title",))   

# Single track schema, when one track needs to be retrieved
track_schema = TrackSchema()
# Multiple track schema, when many tracks need to be retrieved
tracks_schema = TrackSchema(many=True)