from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.conf import settings


class UserSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    full_name = serializers.CharField()
    avatar_uuid = serializers.CharField()


class ListPostSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    media_list = serializers.ListField()
    created_by = UserSerializer()


class PostSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    # All Files must be sent under the same name 'media_list' they will get parsed individually as a list.
    media_list = serializers.ListField(
        child=serializers.FileField(validators=[FileExtensionValidator(settings.MEDIA_FORMATS)], allow_empty_file=False, use_url=False),
        required=True
    )
