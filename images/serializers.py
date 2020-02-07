from rest_framework import serializers
from django.core.validators import FileExtensionValidator


class ImageSerializer(serializers.Serializer):
    image = serializers.FileField(required=True, validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'gif'])])
