from main import ma
from marshmallow import fields

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class RecordSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "album_title", "rpm", "artist_id", "artist")
    artist = fields.Nested("ArtistSchema", only=("artist_name",))

#single card schema, when one card needs to be retrieved
record_schema = RecordSchema()
#multiple card schema, when many cards need to be retrieved
records_schema = RecordSchema(many=True)

