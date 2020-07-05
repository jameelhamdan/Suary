from rest_framework import generics
from main import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin, PaginationMixin


@view_authenticate()
class FeedView(APIViewMixin, PaginationMixin, generics.ListAPIView):
    pagination_kwarg_message = 'Successfully my feed'
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        user = self.request.current_user
        following_ids = user.get_following_queryset().values_list('following_id', flat=True)
        return models.Post.counted.filter(created_by_id__in=following_ids).select_related('created_by').only('content', 'id', 'created_by', 'created_on')
