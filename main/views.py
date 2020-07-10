from rest_framework import generics, parsers
from rest_framework.exceptions import NotFound
from . import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin, PaginationMixin
import media.models
import users.models


@view_authenticate()
class CreatePostView(APIViewMixin, generics.CreateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )
    pagination_kwarg_message = 'Successfully listed my posts!'
    serializer_class = serializers.AddPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user_pk = self.request.current_user.pk
        media_list = cleaned_data.pop('media_list', [])

        # TODO: MOVE this logic to class
        post = models.Post(created_by_id=user_pk, **cleaned_data)

        media_document_list = []
        for uploaded_media in media_list:
            media_document = media.models.MediaDocument(
                parent_id=post.pk,
                parent_type=media.models.MediaDocument.ParentTypes.POST
            )

            media_document.upload(uploaded_media)

            media_document_list.append({
                'hash': media_document.pk,
                'content_type': media_document.content_type
            })

        post.media_list = media_document_list
        post.save()

        serializer = serializers.PostSerializer(post, many=False)
        json_data = serializer.data
        return self.get_response(message='Successfully Added Post', result=json_data)


@view_authenticate()
class ListPostsView(APIViewMixin, PaginationMixin, generics.ListAPIView):
    pagination_kwarg_message = 'Successfully Returned User Posts'
    serializer_class = serializers.PostSerializer

    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        try:
            return users.models.UserData.objects.only('id', 'username').get(username=username)
        except users.models.UserData.DoesNotExist:
            raise NotFound()

    def get_queryset(self):
        user = self.get_object()
        current_user = self.request.current_user

        return models.Post.objects.liked(
            user=current_user
        ).filter(
            created_by_id=user.pk
        ).select_related('created_by').only('content', 'id', 'created_by', 'created_on')


@view_authenticate()
class DetailPostView(APIViewMixin, generics.RetrieveAPIView):
    def get_queryset(self):
        current_user = self.request.current_user
        return models.Post.objects.liked(
            user=current_user
        ).select_related('created_by').only('content', 'id', 'created_by', 'created_on')

    serializer_class = serializers.PostSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.get_response(message='Post Details!', result=serializer.data)


@view_authenticate()
class CreateCommentView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.AddCommentSerializer

    def create(self, request, *args, **kwargs):
        post = generics.get_object_or_404(models.Post.objects, pk=self.kwargs['pk'])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        comment_content = cleaned_data.get('content')
        comment_media = cleaned_data.get('media')
        comment = post.add_comment(comment_content, self.request.current_user, media_file=comment_media)

        serializer = serializers.CommentSerializer(comment, many=False)
        json_data = serializer.data
        return self.get_response(message='Successfully Added Comment', result=json_data)


@view_authenticate()
class ListCommentsView(APIViewMixin, PaginationMixin, generics.ListAPIView):
    pagination_kwarg_message = 'Successfully Returned Post Comments'
    serializer_class = serializers.CommentSerializer

    def get_object(self, *args, **kwargs):
        try:
            return models.Post.objects.only('id').get(pk=self.kwargs['pk'])
        except models.Post.DoesNotExist:
            raise NotFound()

    def get_queryset(self):
        post = self.get_object()
        return models.Comment.objects.filter(post_id=post.pk).select_related('created_by').only('id', 'content', 'post_id', 'created_by', 'created_on')


@view_authenticate()
class LikePostView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.PostLikeSerializer

    def create(self, request, *args, **kwargs):
        post = generics.get_object_or_404(models.Post.objects, pk=self.kwargs['pk'])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        action = cleaned_data['action']
        user_pk = self.request.current_user.pk
        is_liked = None
        if action == self.serializer_class.ACTION_CHOICE_LIKE:
            like = post.add_like(user_pk)
            message = 'Successfully Liked Post'
            is_liked = True
        elif action == self.serializer_class.ACTION_CHOICE_UNLIKE:
            like = post.remove_like(user_pk)
            message = 'Successfully Unliked Post'
            is_liked = False
        else:
            raise Exception('Action Method Not Defined in LikePostView')

        result = {
            'uuid': post.pk,
            'state': is_liked
        }

        return self.get_response(message=message, result=result)
