from django.core.validators import FileExtensionValidator
from django.conf import settings
from rest_framework import serializers
import users.models


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    # full_name = serializers.CharField() # Add When Needed
    avatar_uuid = serializers.CharField()


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[FileExtensionValidator(settings.AVATAR_FORMATS)], allow_empty_file=False, use_url=False, required=True)


class SwitchFollowSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=36, required=True)
    follow = serializers.BooleanField(default=True)

    def validate(self, data):
        user = users.models.UserData.objects.filter(pk=data['user']).first()
        if not user:
            raise serializers.ValidationError({'user': 'User doesn\'t exist!'})

        data['user'] = user
        return data


class ListFollowingSerializer(serializers.Serializer):
    updated_on = serializers.DateTimeField()
    following = UserSerializer()
