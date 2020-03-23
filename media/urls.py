from django.urls import path
from media import views


app_name = 'media'
urlpatterns = [
    path('<str:pk>', views.GetMediaView.as_view(), name='view_media'),
]
