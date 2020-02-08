from django.http.response import Http404
from django.urls import path
from rest_framework import generics, views, parsers, status, response
from . import serializers, models


class UploadMediaView(views.APIView):
    parser_classes = (parsers.MultiPartParser, )

    def post(self, request):
        serializer = serializers.MediaSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            uploaded_media = serializer.validated_data.get('media')
            media_document = models.MediaDocument()

            media_document.upload(uploaded_media)
            media_document.save()

            return response.Response(
                data={
                    'uuid': media_document.uuid
                },
                status=status.HTTP_200_OK
            )


class GetMediaView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        media_uuid = kwargs['uuid']
        media_document = models.MediaDocument.objects(uuid=media_uuid).first()
        if not media_document:
            raise Http404()

        return media_document.stream_media(request=self.request)


urlpatterns = (
    path('upload/', UploadMediaView.as_view()),
    path('<str:uuid>', GetMediaView.as_view(), name='view_media'),
)
