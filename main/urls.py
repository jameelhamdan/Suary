from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('user/<str:username>/posts', views.ListPostsView.as_view(), name='list_user_posts'),
    path('post', views.CreatePostView.as_view(), name='create_post'),
    path('post/<str:pk>', views.DetailPostView.as_view(), name='detail_post'),
    path('post/like', views.LikePostView.as_view(), name='like_post'),
    path('post/comment', views.ListCreateCommentView.as_view(), name='post_comments'),
]
