from django.core.validators import FileExtensionValidator
from django.conf import settings
from rest_framework import serializers


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[FileExtensionValidator(settings.AVATAR_FORMATS)], allow_empty_file=False, use_url=False, required=True)


class SwitchFollowSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=36, required=True)
