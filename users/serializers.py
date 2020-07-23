from django.core.validators import FileExtensionValidator
from django.conf import settings
from rest_framework import serializers
import auth.models


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    full_name = serializers.CharField()
    avatar_url = serializers.SerializerMethodField()
    follow_count = serializers.IntegerField(default=None)
    is_followed = serializers.BooleanField(default=None)

    def get_avatar_url(self, obj):
        if not obj.avatar_uuid:
            return None
        return '%s/%s' % (
            settings.MEDIA_SERVER_BASE_URL,
            obj.avatar_uuid
        )


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[FileExtensionValidator(settings.AVATAR_FORMATS)], allow_empty_file=False, use_url=False, required=True)


class FollowSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=auth.models.User.objects.all(),
        required=True
    )

    ACTION_CHOICE_FOLLOW = 'follow'
    ACTION_CHOICE_UNFOLLOW = 'unfollow'

    ACTION_CHOICES = (
        (ACTION_CHOICE_FOLLOW, 'Like'),
        (ACTION_CHOICE_UNFOLLOW, 'Unlike'),
    )

    action = serializers.ChoiceField(choices=ACTION_CHOICES, required=True)


class ListFollowingSerializer(serializers.Serializer):
    updated_on = serializers.DateTimeField()
    following = UserSerializer()
