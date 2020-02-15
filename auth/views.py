from rest_framework import generics, parsers
from . import serializers
from .backend.decorators import view_allow_any, view_authenticate, view_authenticate_refresh
from _common.mixins import APIViewMixin


@view_allow_any()
class LoginView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, auth_token, refresh_token = serializer.validated_data

        user_data = user.get_data()
        result = {
            'uuid': user.pk,
            'username': user.username,
            'full_name': user_data.full_name,
            'avatar_uuid': user_data.avatar_uuid,
            'auth_token': auth_token,
            'refresh_token': refresh_token,
        }

        return self.get_response(message='Successfully Logged in', result=result)


@view_allow_any()
class RegisterView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        result = {
            'uuid': user.pk,
        }
        return self.get_response(message='Successfully Registered User', result=result)


@view_authenticate()
class ResetPasswordView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.ResetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user, auth_token, refresh_token = serializer.validated_data

        result = {
            'uuid': user.pk,
            'auth_token': auth_token,
            'refresh_token': refresh_token,
        }
        return self.get_response(message='Successfully Updated Password', result=result)


@view_authenticate_refresh()
class RenewAuthTokenView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.RenewAuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_token = serializer.validated_data

        result = {
            'new_token': auth_token,
        }

        return self.get_response(message='Successfully Refreshed Token', result=result)


@view_authenticate_refresh()
class RenewRefreshTokenView(APIViewMixin, generics.CreateAPIView):
    serializer_class = serializers.RenewRefreshTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token, auth_token = serializer.validated_data

        result = {
            'refresh_token': refresh_token,
            'auth_token': auth_token,
        }

        return self.get_response(message='Successfully Refreshed Token', result=result)


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
