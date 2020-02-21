from rest_framework import generics, parsers
from . import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin, PaginationMixin


@view_authenticate()
class UpdateAvatarView(APIViewMixin, generics.UpdateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )
    serializer_class = serializers.UpdateAvatarSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        uploaded_avatar_uuid = self.request.current_user.update_avatar(cleaned_data['avatar'])

        result = {
            'avatar_uuid': uploaded_avatar_uuid,
        }

        return self.get_response(message='Successfully Updated Avatar', result=result)


@view_authenticate()
class FollowView(APIViewMixin, PaginationMixin, generics.ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ListFollowingSerializer
        else:
            return serializers.SwitchFollowSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user = cleaned_data['user']

        if cleaned_data['follow']:
            follow = self.request.current_user.follow(user.pk)
            message = 'Successfully Followed User'
        else:
            follow = self.request.current_user.unfollow(user.pk)
            message = 'Successfully Unfollowed User'

        result = {
            'uuid': user.pk,
        }

        return self.get_response(message=message, result=result)

    def list(self, request, *args, **kwargs):
        user_pk = self.request.current_user.pk
        queryset = models.Follow.objects.filter(follower_id=user_pk).only('following', 'updated_on')

        json_data = self.paginate_queryset(queryset)
        return self.get_response(message='Successfully Returned Users i follow.', result=json_data)
