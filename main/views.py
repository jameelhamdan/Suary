from rest_framework import generics, parsers
from rest_framework.exceptions import NotFound
from . import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin, PaginationMixin
import media.models


@view_authenticate()
class ListCreatePostView(APIViewMixin, PaginationMixin, generics.ListCreateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )
    pagination_kwarg_message = 'Successfully listed my posts!'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ListPostSerializer
        else:
            return serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user_pk = self.request.current_user.pk
        media_list = cleaned_data.pop('media_list', [])

        post = models.Post(created_by_id=user_pk, **cleaned_data)
        post.save()

        for uploaded_media in media_list:
            media_document = media.models.MediaDocument(parent_id=post.pk)
            media_document.upload(uploaded_media)

            post.media_list.append(media_document.pk)

        post.save()

        serializer = serializers.ListPostSerializer(post, many=False)
        json_data = serializer.data
        return self.get_response(message='Successfully Added Post', result=json_data)

    def get_queryset(self):
        user_pk = self.request.current_user.pk
        queryset = models.Post.objects.filter(created_by_id=user_pk).select_related('created_by').only('content', 'media_list', 'created_by', 'created_on', 'tags')
        return queryset


@view_authenticate()
class ListCreateCommentView(APIViewMixin, PaginationMixin, generics.ListCreateAPIView):
    pagination_kwarg_message = 'Successfully Returned Post Comments'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ListCommentSerializer
        else:
            return serializers.CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user = self.request.current_user

        post = cleaned_data['post']
        comment = post.add_comment(cleaned_data['content'], user)

        serializer = serializers.ListCommentSerializer(comment, many=False)
        json_data = serializer.data
        return self.get_response(message='Successfully Added Comment', result=json_data)

    def get_queryset(self):
        # TODO: get a better way of doing this
        post_pk = self.request.POST.get('post_id', None)

        if not post_pk:
            raise NotFound()

        return models.Comment.objects.filter(post_id=post_pk).select_related('created_by').only('content', 'post_id', 'created_by', 'created_on')


@view_authenticate()
class LikePostView(APIViewMixin, PaginationMixin, generics.ListCreateAPIView):
    serializer_class = serializers.SwitchPostLikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        post = cleaned_data['post']
        user_pk = self.request.current_user.pk

        if cleaned_data['like']:
            like = post.add_like(user_pk)
            message = 'Successfully Liked Post'
        else:
            like = post.remove_like(user_pk)
            message = 'Successfully Unliked Post'

        result = {
            'uuid': post.pk,
        }

        return self.get_response(message=message, result=result)
