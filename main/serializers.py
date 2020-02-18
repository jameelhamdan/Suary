from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.conf import settings
import users.serializers


class ListPostSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    media_list = serializers.ListField()
    created_by = users.serializers.UserSerializer()


class PostSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    # All Files must be sent under the same name 'media_list' they will get parsed individually as a list.
    media_list = serializers.ListField(
        child=serializers.FileField(validators=[FileExtensionValidator(settings.MEDIA_FORMATS)], allow_empty_file=False, use_url=False),
        required=True
    )
