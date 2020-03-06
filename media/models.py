from django.http.response import FileResponse, StreamingHttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.conf import settings
import djongo.models as mongo
from djongo import storage
from _common import utils, images


class MediaDocument(mongo.Model):
    collection_name = 'media'
    database_name = 'media'
    objects = mongo.DjongoManager()

    id = mongo.CharField(max_length=36, db_column='_id', primary_key=True, default=utils.generate_uuid)
    media = mongo.FileField(storage=storage.GridFSStorage(collection=collection_name, database=database_name))
    content_type = mongo.TextField()
    length = mongo.IntegerField()
    created_on = mongo.DateTimeField(default=timezone.now)
    parent_id = mongo.CharField(max_length=36, null=True)

    def get_url(self):
        return reverse_lazy('view_media', kwargs={'pk': self.pk})

    def stream(self):
        return self.media.file

    def stream_image(self, request, *args, **kwargs):
        stream = self.stream()
        response = FileResponse(stream, content_type=self.content_type)
        return utils.stream_response(request, response, self.length)

    def stream_video(self, request, *args, **kwargs):
        stream = self.stream()
        response = FileResponse(stream, content_type=self.content_type)
        return utils.stream_response(request, response, self.length)

    def stream_media(self, *args, **kwargs):
        try:
            content_type = self.content_type.split('/')[0]
        except AttributeError:
            raise Exception('Unknown media type')

        if content_type == 'image':
            return self.stream_image(*args, **kwargs)
        elif content_type == 'video':
            return self.stream_video(*args, **kwargs)
        else:
            raise Exception('Media type not supported')

    def upload(self, upload_stream):
        #upload_stream = images.optimize_media(upload_stream)
        self.media = upload_stream
        self.content_type = upload_stream.content_type
        self.length = upload_stream.size
        self.save()
        return self

    class Meta:
        db_table = 'media'
        db = settings.MEDIA_DATABASE
