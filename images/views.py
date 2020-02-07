from django.urls import path
from django.http.response import StreamingHttpResponse, Http404, HttpResponse
from rest_framework import generics, views, parsers, status, response
from . import serializers, models


class UploadImageView(views.APIView):
    parser_classes = (parsers.MultiPartParser, )

    def post(self, request):
        serializer = serializers.ImageSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            uploaded_image = serializer.validated_data.get('image')
            imageDocument = models.Image()

            imageDocument.image.put(uploaded_image, content_type=uploaded_image.content_type)
            imageDocument.save()

            return response.Response(
                data={
                    'uuid': imageDocument.uuid
                },
                status=status.HTTP_200_OK
            )


class GetImageView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        image_uuid = kwargs['uuid']
        imageDocument = models.Image.objects(uuid=image_uuid).first()
        if not imageDocument:
            raise Http404()

        image = imageDocument.image
        return StreamingHttpResponse(imageDocument.stream_image_bytes(), content_type=image.content_type)


urlpatterns = (
    path('upload/', UploadImageView.as_view()),
    path('<str:uuid>/', GetImageView.as_view()),
)
