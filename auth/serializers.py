from django.core.validators import FileExtensionValidator
from django.conf import settings
from rest_framework import serializers
from .models import User
from .backend import jwt, utils
from .backend.jwt import create_auth_token, create_refresh_token
from _common import validators


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get('username', None)
        email = data.get('email', None)

        user = None

        if not username and not email:
            raise serializers.ValidationError(u'You must provide an email or username')

        if username and email:
            raise serializers.ValidationError(u'You must only provide email or username not both')

        if username:
            user = User.objects.filter(username=username).first()

        elif email:
            user = User.objects.filter(email=email).first()

        if user is None or not user.validate_password(data['password']):
            raise serializers.ValidationError(u'Password or username is incorrect')

        user.update_last_login()
        auth_token = create_auth_token(user.pk)
        refresh_token = create_refresh_token(user.pk, user.get_secret_key())

        return user, auth_token, refresh_token


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, validators=[validators.UsernameValidator()])
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    full_name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)

    def validate(self, data):
        super(RegisterSerializer, self).validate(data)
        # Validate Password

        if not data['password'] == data['password_confirm']:
            raise serializers.ValidationError(u'Password Don\'t match!')

        # check for users with same email or username
        username = data['username']
        email = data['email']

        if User.exists(username, email):
            raise serializers.ValidationError(u'This Email or Username is already registered!')

        user = User.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            full_name=data['full_name'],
            birth_date=data['birth_date'],
        )

        return user


class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        # Validate Password
        user = self.context['request'].current_user

        if not data['new_password'] == data['new_password_confirm']:
            raise serializers.ValidationError(u'Password Don\'t match!')

        if not user.validate_password(data['old_password']):
            raise serializers.ValidationError(u'Password Incorrect!')

        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError(u'New Password must be different than old password')

        user.set_password(data['new_password'])
        user.reset_secret_key()
        user.update_last_login()
        auth_token = create_auth_token(user.pk)
        refresh_token = create_refresh_token(user.pk, user.get_secret_key())

        return user, auth_token, refresh_token


class RenewAuthTokenSerializer(serializers.Serializer):
    def validate(self, data):
        user = self.context['request'].current_user

        old_token = utils.get_auth_header(self.context['request'])
        new_token = jwt.renew_auth_token(old_token, user.get_secret_key())
        return new_token


class RenewRefreshTokenSerializer(serializers.Serializer):
    def validate(self, data):
        user = self.context['request'].current_user
        
        old_token = utils.get_auth_header(self.context['request'])
        new_refresh_token = jwt.renew_refresh_token(old_token, user.get_secret_key())
        new_auth_token = jwt.renew_auth_token(old_token, user.get_secret_key())

        return new_refresh_token, new_auth_token


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[FileExtensionValidator(settings.AVATAR_FORMATS)], allow_empty_file=False, use_url=False, required=True)
