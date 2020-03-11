from django.conf import settings
from django.urls import path, re_path, include
from django.views.decorators.cache import never_cache
import frontend.views

api_prefix = settings.API_PREFIX
urlpatterns = [
    path(api_prefix + '/auth/', include('auth.urls')),
    path(api_prefix + '/users/', include('users.urls')),
    path(api_prefix + '/main/', include('main.urls')),
    path('media/', include('media.urls')),
]


urlpatterns += [
    re_path(r'^.*', never_cache(frontend.views.IndexView.as_view()), name='index')
]
