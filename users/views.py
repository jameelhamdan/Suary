from rest_framework import generics, parsers
from . import serializers
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin


@view_authenticate()
class UpdateAvatarView(APIViewMixin, generics.UpdateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )
    serializer_class = serializers.UpdateAvatarSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        uploaded_avatar_uuid = self.request.current_user.update_avatar(cleaned_data['avatar'])

        result = {
            'avatar_uuid': uploaded_avatar_uuid,
        }

        return self.get_response(message='Successfully Updated Avatar', result=result)
