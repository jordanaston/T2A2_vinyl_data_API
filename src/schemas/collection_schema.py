from main import ma

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CollectionSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "user_id", "record_id")

#single card schema, when one card needs to be retrieved
collection_schema = CollectionSchema()
#multiple card schema, when many cards need to be retrieved
collections_schema = CollectionSchema(many=True)