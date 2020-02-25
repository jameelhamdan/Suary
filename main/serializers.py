from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.conf import settings
from . import models
import users.serializers


class ListPostSerializer(serializers.Serializer):
    id = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    tags = serializers.ListField()
    media_list = serializers.ListField()
    created_by = users.serializers.UserSerializer()


class PostSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    # All Files must be sent under the same name 'media_list' they will get parsed individually as a list.
    media_list = serializers.ListField(
        child=serializers.FileField(validators=[FileExtensionValidator(settings.MEDIA_FORMATS)], allow_empty_file=False, use_url=False),
        required=False
    )


class ListCommentSerializer(serializers.Serializer):
    id = serializers.CharField()
    post_id = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    created_by = users.serializers.UserSerializer()


class CommentSerializer(serializers.Serializer):
    post_id = serializers.CharField(max_length=36, required=True)
    content = serializers.CharField(required=True)

    def validate(self, data):
        post = models.Post.objects.filter(pk=data['post_id']).first()
        if not post:
            raise serializers.ValidationError({'post': 'Post doesn\'t exist!'})

        data['post'] = post
        return data


class SwitchPostLikeSerializer(serializers.Serializer):
    post_id = serializers.CharField(max_length=36, required=True)
    like = serializers.BooleanField(default=True)

    def validate(self, data):
        post = models.Post.objects.filter(pk=data['post_id']).first()
        if not post:
            raise serializers.ValidationError({'post': 'Post doesn\'t exist!'})

        data['post'] = post
        return data
