from main import ma
from marshmallow.validate import Length, Range
from marshmallow import fields

# Track Schema created with Marshmallow, providing serialization needed for converting the data into JSON
class TrackSchema(ma.Schema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Fields to expose
        fields = ("id", "track_title", "bpm", "key", "record_id", "record")
    # Schema nesting: adds album_title to the response     
    record = fields.Nested("RecordSchema", only=("album_title",))   
    # Add length validation for track_title 
    track_title = ma.String(validate=Length(min=1, max=100))
    # Add range validation for bpm 
    bpm = ma.Integer(validate=Range(min=1, max=300))
    # Add length validation for key 
    key = ma.String(validate=Length(min=1, max=20))
# Single track schema, when one track needs to be retrieved
track_schema = TrackSchema()
# Multiple track schema, when many tracks need to be retrieved
tracks_schema = TrackSchema(many=True)