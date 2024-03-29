from rest_framework import generics
from main import serializers, models
from auth.backend.decorators import view_authenticate
from _common.mixins import APIViewMixin, PaginationMixin


@view_authenticate()
class FeedView(APIViewMixin, PaginationMixin, generics.ListAPIView):
    pagination_kwarg_message = 'Successfully returned my feed'
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        current_user = self.request.current_user
        created_by_prefetch = current_user.related_prefetch('created_by')

        following_ids = current_user.get_following_queryset().values_list('following_id', flat=True)
        return models.Post.objects.liked(user=current_user).filter(
            created_by_id__in=following_ids
        ).prefetch_related(created_by_prefetch).only('id', 'content', 'created_by', 'created_on')


@view_authenticate()
class SearchView(APIViewMixin, PaginationMixin, generics.ListAPIView):
    pagination_kwarg_message = 'Successfully returned serach'
    serializer_class = serializers.PostSerializer

    def get_search_query(self):
        return self.request.GET.get('q', None)

    def get_queryset(self):
        current_user = self.request.current_user
        created_by_prefetch = current_user.related_prefetch('created_by')

        return models.Post.objects.search(
            search_query=self.get_search_query()
        ).prefetch_related(created_by_prefetch).liked(
            user=current_user
        ).only('id', 'content', 'created_by', 'created_on')
