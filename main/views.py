from rest_framework import generics, parsers
from . import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin
import media.models


@view_authenticate()
class ListCreatePostView(APIViewMixin, generics.ListCreateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user_pk = self.request.current_user.pk
        media_list = cleaned_data.pop('media_list')

        post = models.Post(created_by=user_pk, **cleaned_data)
        post.save()

        for uploaded_media in media_list:
            media_document = media.models.MediaDocument(parent=post)
            media_document.upload(uploaded_media)

            post.media_list.append(media_document.pk)

        post.save()

        serializer = serializers.ListPostSerializer(post, many=False)
        json_data = serializer.data
        return self.get_response(message='Successfully Added Post', result=json_data)

    def paginate_queryset(self, queryset):
        page = self.request.GET.get('page', 0)
        limit = self.request.GET.get('limit', 10)

        records_per_page = limit
        offset = (page - 1) * records_per_page

        queryset = list(queryset.skip(offset).limit(records_per_page + 1))

        serializer = serializers.ListPostSerializer(queryset[:records_per_page], many=True)

        json_data = serializer.data
        request_data = {
            'page': page,
            'first': page == 1,
            'last': len(queryset) == records_per_page + 1,
            'list': json_data,
        }
        return request_data

    def list(self, request, *args, **kwargs):
        user_pk = self.request.current_user.pk
        queryset = models.Post.objects.filter(created_by=user_pk).only('content', 'media_list', 'created_by', 'created_on')

        json_data = self.paginate_queryset(queryset)
        return self.get_response(message='Successfully Returned My Posts', result=json_data)
