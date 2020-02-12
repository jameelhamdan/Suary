from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    full_name = serializers.CharField()


class ListPostSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    media_uuid = serializers.ListField()
    created_by = UserSerializer()


class PostSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
