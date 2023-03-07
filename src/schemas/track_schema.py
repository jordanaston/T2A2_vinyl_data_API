from main import ma

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class TrackSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "track_title", "bpm", "key", "record_id")

#single card schema, when one card needs to be retrieved
track_schema = TrackSchema()
#multiple card schema, when many cards need to be retrieved
tracks_schema = TrackSchema(many=True)