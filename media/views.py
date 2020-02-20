from django.http.response import Http404
from auth.backend.decorators import view_allow_any
from rest_framework import views, parsers
from . import models


@view_allow_any()
class GetMediaView(views.APIView):
    def get(self, *args, **kwargs):
        media_pk = self.kwargs['pk']
        media_document = models.MediaDocument.objects.filter(pk=media_pk).first()
        if not media_document:
            raise Http404()

        return media_document.stream_media(request=self.request)
