from django.core.validators import FileExtensionValidator
from django.conf import settings
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    full_name = serializers.CharField()
    avatar_uuid = serializers.CharField()


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[FileExtensionValidator(settings.AVATAR_FORMATS)], allow_empty_file=False, use_url=False, required=True)


class SwitchFollowSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=36, required=True)
    follow = serializers.BooleanField(default=True)


class ListFollowingSerializer(serializers.Serializer):
    updated_on = serializers.DateTimeField()
    following = UserSerializer()
