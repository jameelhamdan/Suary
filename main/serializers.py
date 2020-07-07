from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.conf import settings
from . import models
import users.serializers


class MediaSerializer(serializers.Serializer):
    hash = serializers.CharField()
    content_type = serializers.CharField()


class PostSerializer(serializers.Serializer):
    id = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    tags = serializers.ListField()
    media_list = serializers.ListField(
        child=MediaSerializer()
    )
    created_by = users.serializers.UserSerializer()
    likes_count = serializers.CharField()
    comments_count = serializers.CharField()
    is_liked = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        # TODO: Remove this after djongo fix
        if len(obj.user_likes) > 0:
            return True
        else:
            return False


# Used for Adding a post
class AddPostSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    # All Files must be sent under the same name 'media_list' they will get parsed individually as a list.
    media_list = serializers.ListField(
        child=serializers.FileField(validators=[FileExtensionValidator(settings.MEDIA_FORMATS)], allow_empty_file=False, use_url=False),
        allow_empty=False,
        required=False
    )


class CommentSerializer(serializers.Serializer):
    id = serializers.CharField()
    post_id = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    created_by = users.serializers.UserSerializer()
    media = MediaSerializer(default=None)


class AddCommentSerializer(serializers.Serializer):
    content = serializers.CharField(required=False)
    media = serializers.FileField(validators=[FileExtensionValidator(settings.IMAGE_FORMATS)], allow_empty_file=False, use_url=False, required=False)


class SwitchPostLikeSerializer(serializers.Serializer):
    ACTION_CHOICE_LIKE = 'like'
    ACTION_CHOICE_UNLIKE = 'unlike'

    ACTION_CHOICES = (
        (ACTION_CHOICE_LIKE, 'Like'),
        (ACTION_CHOICE_UNLIKE, 'Unlike'),
    )

    post = serializers.SlugRelatedField(slug_field='pk', queryset=models.Post.objects.all(), required=True)
    action = serializers.ChoiceField(choices=ACTION_CHOICES, required=True)
