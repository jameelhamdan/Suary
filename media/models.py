from django.utils import timezone
from django.urls import reverse_lazy
from django.http.response import StreamingHttpResponse, HttpResponse
from _common.utils import generate_uuid
import mongoengine as mongo
import gridfs


class MediaDocument(mongo.Document):
    uuid = mongo.StringField(unique=True, max_length=36, default=generate_uuid)
    created_on = mongo.DateTimeField(default=timezone.now())
    media = mongo.FileField(collection_name='media')

    def get_url(self):
        return reverse_lazy('view_media', kwargs={'uuid': self.uuid})

    def stream_image(self, **kwargs):
        fs_bucket = gridfs.GridFSBucket(self._get_db(), self._get_collection_name())
        stream = fs_bucket.open_download_stream(self.media.grid_id)

        return StreamingHttpResponse(stream, content_type=self.media.content_type)

    def stream_video(self, **kwargs):
        fs_bucket = gridfs.GridFSBucket(self._get_db(), self._get_collection_name())
        stream = fs_bucket.open_download_stream(self.media.grid_id)

        return StreamingHttpResponse(stream, content_type=self.media.content_type)

    def stream_media(self, **kwargs):
        content_type = self.media.content_type.split('/')[0]
        if content_type == 'image':
            return self.stream_image(**kwargs)
        if content_type == 'video':
            return self.stream_video(**kwargs)
        else:
            raise Exception('Media type not supported')

    meta = {
        'indexes': [
            'uuid'
        ],
        'db_alias': 'media_database',
        'collection': 'media',
    }
