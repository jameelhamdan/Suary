from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('me/post', views.ListCreatePostView.as_view(), name='post'),
]
