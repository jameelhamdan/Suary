from django.urls import path
from django.http.response import Http404
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
            mediaDocument = models.MediaDocument()

            mediaDocument.media.put(uploaded_media, content_type=uploaded_media.content_type)
            mediaDocument.save()

            return response.Response(
                data={
                    'uuid': mediaDocument.uuid
                },
                status=status.HTTP_200_OK
            )


class GetMediaView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        media_uuid = kwargs['uuid']
        mediaDocument = models.MediaDocument.objects(uuid=media_uuid).first()
        if not mediaDocument:
            raise Http404()

        return mediaDocument.stream_media()


urlpatterns = (
    path('upload/', UploadMediaView.as_view()),
    path('<str:uuid>', GetMediaView.as_view(), name='view_media'),
)
