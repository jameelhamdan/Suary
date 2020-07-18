from rest_framework import generics, parsers
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin, PaginationMixin
from . import serializers, models
import auth.models


@view_authenticate()
class UpdateAvatarView(APIViewMixin, generics.UpdateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )
    serializer_class = serializers.UpdateAvatarSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user = self.request.current_user
        user.update_avatar(cleaned_data['avatar'])

        result = {
            'avatar_url': user.get_avatar_url(),
        }

        return self.get_response(message='Successfully Updated Avatar', result=result)


@view_authenticate()
class FollowView(APIViewMixin, PaginationMixin, generics.ListCreateAPIView):
    pagination_kwarg_message = 'Successfully Returned Users i follow.'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ListFollowingSerializer
        else:
            return serializers.FollowSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user = cleaned_data['user']
        action = cleaned_data['action']
        serializer_class = self.get_serializer_class()

        if action == serializer_class.ACTION_CHOICE_FOLLOW:
            follow = self.request.current_user.follow(user.pk)
            new_state = True
            message = 'Successfully Followed User'
        elif action == serializer_class.ACTION_CHOICE_UNFOLLOW:
            follow = self.request.current_user.unfollow(user.pk)
            new_state = False
            message = 'Successfully Unfollowed User'
        else:
            raise Exception('Action Method Not Defined in FollowView')

        result = {
            'id': user.pk,
            'state': new_state
        }

        return self.get_response(message=message, result=result)

    def get_queryset(self):
        user_pk = self.request.current_user.pk
        return models.Follow.objects.filter(follower_id=user_pk).only('following', 'updated_on')


@view_authenticate()
class DetailUserView(APIViewMixin, generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.get_response(message='User Details!', result=serializer.data)

    def get_queryset(self):
        return auth.models.User.objects.related(self.request.current_user)
