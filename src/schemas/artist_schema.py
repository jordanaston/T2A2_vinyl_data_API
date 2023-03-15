from main import ma

# Artist Schema created with Marshmallow, providing serialization needed for converting the data into JSON
class ArtistSchema(ma.Schema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Fields to expose
        fields = ("id", "artist_name")
    
# Single artist schema, when one artist needs to be retrieved
artist_schema = ArtistSchema()
# Multiple artists schema, when many artists need to be retrieved
artists_schema = ArtistSchema(many=True)