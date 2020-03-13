from django.conf import settings
from django.urls import path, re_path, include
from django.views.decorators.cache import never_cache
import frontend.views

api_prefix = settings.API_PREFIX
excludes_string = ''

for route in [api_prefix, 'media', 'admin']:
    excludes_string += f'(?!{route}/)'

exclude_regex = fr'^{excludes_string}[\w\/]+$'

urlpatterns = [
    path(api_prefix + '/auth/', include('auth.urls')),
    path(api_prefix + '/users/', include('users.urls')),
    path(api_prefix + '/main/', include('main.urls')),
    path('media/', include('media.urls')),
]


urlpatterns += [
    re_path(exclude_regex, never_cache(frontend.views.IndexView.as_view()), name='index'),
    path('', never_cache(frontend.views.IndexView.as_view()), name='index')
]
