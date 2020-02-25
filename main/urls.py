from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('post', views.ListCreatePostView.as_view(), name='post'),
    path('post/like', views.LikePostView.as_view(), name='like_post'),
    path('post/comment', views.ListCreateCommentView.as_view(), name='post_comments'),
]
