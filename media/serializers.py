from rest_framework import serializers
from django.core.validators import FileExtensionValidator

MEDIA_FORMATS = ['png', 'jpeg', 'jpg', 'gif', 'mp4', 'm4a', 'm4v', 'webm']


class MediaSerializer(serializers.Serializer):
    media = serializers.FileField(required=True, validators=[FileExtensionValidator(MEDIA_FORMATS)])
