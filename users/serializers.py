from django.core.validators import FileExtensionValidator
from django.conf import settings
from rest_framework import serializers
import auth.models


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    # full_name = serializers.CharField() # Add When Needed
    avatar_uuid = serializers.CharField()


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[FileExtensionValidator(settings.AVATAR_FORMATS)], allow_empty_file=False, use_url=False, required=True)


class SwitchFollowSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=auth.models.User.objects.all(),
        required=True
    )
    follow = serializers.BooleanField(default=True)


class ListFollowingSerializer(serializers.Serializer):
    updated_on = serializers.DateTimeField()
    following = UserSerializer()
