from main import ma

# Collection Schema created with Marshmallow, providing serialization needed for converting the data into JSON
class CollectionSchema(ma.Schema):
    class Meta:
        # Orders the response from alphabetical to the order of the fields
        ordered = True
        # Fields to expose
        fields = ("id", "user_id", "record_id")

# Single collection schema, when one collection needs to be retrieved
collection_schema = CollectionSchema()
# Multiple collections schema, when many collections need to be retrieved
collections_schema = CollectionSchema(many=True)