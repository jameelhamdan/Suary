from django.urls import path, include


urlpatterns = [
    path('auth/', include('auth.urls')),
    path('media/', include('media.urls')),
    path('main/', include('main.urls')),
]
