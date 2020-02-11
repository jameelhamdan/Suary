from rest_framework import generics
from . import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin


@view_authenticate()
class AddPostView(APIViewMixin, generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cleaned_data = serializer.validated_data

        user_pk = self.request.current_user.pk
        post = models.Post(created_by=user_pk, **cleaned_data)
        post.save()

        result = {
            'uuid': post.uuid,
            'content': post.content,
        }

        return self.get_response(message='Successfully Added Post', result=result)

    def list(self, request, *args, **kwargs):
        user_pk = self.request.current_user.pk
        queryset = models.Post.objects.filter(created_by=user_pk).only('content', 'created_by', 'created_on')

        return self.get_response(message='Successfully Returned My Posts', result=list(queryset))
