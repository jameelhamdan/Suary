from django.utils import timezone
from _common.utils import generate_uuid
import mongoengine as mongo
import gridfs


class Image(mongo.Document):
    uuid = mongo.StringField(unique=True, max_length=36, default=generate_uuid)
    created_on = mongo.DateTimeField(default=timezone.now())
    image = mongo.FileField(collection_name='images')

    def stream_image_bytes(self):
        fs_bucket = gridfs.GridFSBucket(self._get_db(), self._get_collection_name())
        return fs_bucket.open_download_stream(self.image.grid_id)

    meta = {
        'indexes': [
            'uuid'
        ],
        'db_alias': 'image_database',
        'collection': 'images',
    }
