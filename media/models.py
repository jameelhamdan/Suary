from django.http.response import FileResponse, StreamingHttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from _common.utils import generate_uuid
import mongoengine as mongo
import gridfs
from gridfs import GridIn
from _common import utils


class MediaDocument(mongo.Document):
    uuid = mongo.StringField(unique=True, max_length=36, default=generate_uuid)
    created_on = mongo.DateTimeField(default=timezone.now())
    media = mongo.FileField(collection_name='media')

    def get_url(self):
        return reverse_lazy('view_media', kwargs={'uuid': self.uuid})

    def stream_image(self, *args, **kwargs):
        fs_bucket = gridfs.GridFSBucket(self._get_db(), self._get_collection_name())
        stream = fs_bucket.open_download_stream(self.media.grid_id)

        return StreamingHttpResponse(stream, content_type=self.media.content_type)

    def stream_video(self, request, *args, **kwargs):
        fs_bucket = gridfs.GridFSBucket(self._get_db(), self._get_collection_name())
        stream = fs_bucket.open_download_stream(self.media.grid_id)

        response = FileResponse(stream, content_type=self.media.content_type)
        return utils.stream_response(request, response, self.media.length)

    def stream_media(self, *args, **kwargs):
        try:
            content_type = self.media.content_type.split('/')[0]
        except AttributeError:
            raise Exception('Unknown media type')

        if content_type == 'image':
            return self.stream_image(*args, **kwargs)
        if content_type == 'video':
            return self.stream_video(*args, **kwargs)
        else:
            raise Exception('Media type not supported')

    def upload(self, upload_stream):
        self.media.put(upload_stream, content_type=upload_stream.content_type)
        return

        # TODO fix this code
        # fs_bucket = gridfs.GridFSBucket(self._get_db(), self._get_collection_name())
        #
        # kwargs = {
        #     'chunk_size': (fs_bucket._chunk_size_bytes),
        #     'content_type': upload_stream.content_type,
        # }
        #
        # grid_in = GridIn(fs_bucket._collection, disable_md5=fs_bucket._disable_md5, **kwargs)
        #
        # try:
        #     grid_in.write(upload_stream)
        # finally:
        #     grid_in.close()
        #
        # self.media = self.media.grid_id
        # return self.media.grid_id

    meta = {
        'indexes': [
            'uuid'
        ],
        'db_alias': 'media_database',
        'collection': 'media',
    }
