from main import ma
from marshmallow import fields

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ArtistSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "artist_name")
    
#single card schema, when one card needs to be retrieved
artist_schema = ArtistSchema()
#multiple card schema, when many cards need to be retrieved
artists_schema = ArtistSchema(many=True)