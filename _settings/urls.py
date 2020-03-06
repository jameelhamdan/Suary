from django.conf import settings
from django.urls import path, include


api_prefix = settings.API_PREFIX
urlpatterns = [
    path(api_prefix + '/auth/', include('auth.urls')),
    path(api_prefix + '/media/', include('media.urls')),
    path(api_prefix + '/users/', include('users.urls')),
    path(api_prefix + '/main/', include('main.urls')),
    path('', include('frontend.urls')),
]
