from django.conf import settings
from django.utils import timezone
from pymongo import MongoClient
import gridfs
import uuid


class MongoConnection(object):

    def __init__(self):
        client = MongoClient(settings.MONGO_DB_IMAGE_DATABASE_HOST, settings.MONGO_DB_IMAGE_DATABASE_PORT)
        self.db = client[settings.MONGO_DB_IMAGE_DATABASE_NAME]

    def get_collection(self, name):
        self.collection = self.db['{}.files'.format(name)]


class ImageCollection(MongoConnection):
    collection_name = 'images'

    def __init__(self):
        super(ImageCollection, self).__init__()
        self.get_collection(self.collection_name)
        self.fs = gridfs.GridFS(self.db, self.collection_name)
        self.fs_bucket = gridfs.GridFSBucket(self.db, self.collection_name)

    def save(self, file):
        image_uuid = uuid.uuid4().hex

        doc = {
            'uuid': image_uuid,
            'created_on': timezone.now()
        }

        filename = '{}.{}'.format(image_uuid, file.content_type.rsplit('/', -1)[1])
        self.fs.put(file, filename=filename, content_type=file.content_type, **doc)

        return image_uuid

    def get_image(self, uuid):
        image_on_db = self.collection.find_one({'uuid': uuid})
        if not image_on_db:
            return None, None

        image_out = self.fs_bucket.open_download_stream(image_on_db['_id'])

        return image_out, image_on_db['contentType']

    def remove(self, uuid):
            if self.collection.find({'uuid': uuid}).count():
                self.collection.delete_one({'uuid': uuid})
