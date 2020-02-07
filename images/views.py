from django.urls import path
from django.http.response import StreamingHttpResponse, Http404
from rest_framework import views, parsers, status, response
from . import serializers, db_client


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
            image_data = serializer.validated_data.get('image')
            client = db_client.ImageCollection()
            image_uuid = client.save(image_data)

            return response.Response(
                data={
                    'uuid': image_uuid
                },
                status=status.HTTP_200_OK
            )


class GetImageView(views.APIView):

    def get(self, *args, **kwargs):
        image_uuid = kwargs['uuid']
        client = db_client.ImageCollection()
        result, content_type = client.get_image(image_uuid)
        if not content_type:
            return Http404()

        return StreamingHttpResponse(result, content_type=content_type)


urlpatterns = (
    path('upload/', UploadImageView.as_view()),
    path('<str:uuid>/', GetImageView.as_view()),
)
