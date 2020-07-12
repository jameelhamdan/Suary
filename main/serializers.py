from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.conf import settings
import users.serializers


class MediaSerializer(serializers.Serializer):
    hash = serializers.CharField()
    content_type = serializers.CharField()


class PostSerializer(serializers.Serializer):
    id = serializers.CharField()
    content = serializers.CharField()
    tags = serializers.ListField(
        child=serializers.CharField()
    )
    media_list = MediaSerializer(
        source='media',
        many=True
    )

    created_on = serializers.DateTimeField()
    created_by = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(default=None)
    comments_count = serializers.IntegerField(default=None)
    is_liked = serializers.BooleanField(default=None)

    def get_created_by(self, obj):
        # TODO: do this a better way
        if hasattr(obj, 'created_by_rel'):
            created_by = obj.created_by_rel
        else:
            created_by = obj.created_by
        return users.serializers.UserSerializer(created_by).data


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
    created_by = serializers.SerializerMethodField()
    media = MediaSerializer(default=None)

    def get_created_by(self, obj):
        # TODO: do this a better way
        if hasattr(obj, 'created_by_rel'):
            created_by = obj.created_by_rel
        else:
            created_by = obj.created_by
        return users.serializers.UserSerializer(created_by).data


class AddCommentSerializer(serializers.Serializer):
    content = serializers.CharField(required=False, default='')
    media = serializers.FileField(validators=[FileExtensionValidator(settings.IMAGE_FORMATS)], allow_empty_file=False, use_url=False, required=False)


class PostLikeSerializer(serializers.Serializer):
    ACTION_CHOICE_LIKE = 'like'
    ACTION_CHOICE_UNLIKE = 'unlike'

    ACTION_CHOICES = (
        (ACTION_CHOICE_LIKE, 'Like'),
        (ACTION_CHOICE_UNLIKE, 'Unlike'),
    )

    action = serializers.ChoiceField(choices=ACTION_CHOICES, required=True)
