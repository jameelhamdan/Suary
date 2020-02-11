from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('post', views.AddPostView.as_view(), name='post'),
]
