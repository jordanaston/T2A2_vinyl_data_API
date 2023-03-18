from main import ma
from marshmallow.validate import Length
from marshmallow import pre_load
import html

# Artist Schema created with Marshmallow, providing serialization needed for converting the data into JSON
class ArtistSchema(ma.Schema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Fields to expose
        fields = ("id", "artist_name")
    # Add length validation for artist_name 
    artist_name = ma.String(validate=Length(min=1, max=100))

    # Sanitization function to escape special characters in artist_name
    @pre_load
    def sanitize_artist_name(self, data, **kwargs):
        if "artist_name" in data:
            data["artist_name"] = html.escape(data["artist_name"].strip())
        return data
        
# Single artist schema, when one artist needs to be retrieved
artist_schema = ArtistSchema()
# Multiple artists schema, when many artists need to be retrieved
artists_schema = ArtistSchema(many=True)