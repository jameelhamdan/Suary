from django.http.response import Http404
from auth.backend.decorators import view_allow_any
from rest_framework import generics
from . import models


@view_allow_any()
class GetMediaView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        media_uuid = self.kwargs['uuid']
        media_document = models.MediaDocument.objects(uuid=media_uuid).first()
        if not media_document:
            raise Http404()

        return media_document.stream_media(request=self.request)
