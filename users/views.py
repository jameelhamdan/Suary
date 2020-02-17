from rest_framework import generics, parsers
from . import serializers
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin


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


class FollowView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.SwitchFollowSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user_pk = cleaned_data['user']
        follow = self.request.user.follow(user_pk)

        result = {
            'uuid': user_pk,
        }

        return self.get_response(message='Successfully Followed User', result=result)


class UnFollowView(FollowView):
    serializer_class = serializers.SwitchFollowSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user_pk = cleaned_data['user']
        follow = self.request.user.follow(user_pk)

        result = {
            'uuid': user_pk,
        }

        return self.get_response(message='Successfully Unfollowed User', result=result)
