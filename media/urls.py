from django.urls import path
from media import views


app_name = 'media'
urlpatterns = [
    path('upload/', views.UploadMediaView.as_view(), name='upload_media'),
    path('<str:uuid>', views.GetMediaView.as_view(), name='view_media'),
]
