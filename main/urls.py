from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('user/<str:username>/posts', views.ListPostsView.as_view(), name='list_user_posts'),
    path('post', views.CreatePostView.as_view(), name='create_post'),
    path('post/<str:pk>', views.DetailPostView.as_view(), name='detail_post'),
    path('post/<str:pk>/comments', views.ListCommentsView.as_view(), name='post_comments'),
    path('post/<str:pk>/comments/add', views.CreateCommentView.as_view(), name='post_comments'),
    path('post/<str:pk>/likes/add', views.LikePostView.as_view(), name='like_post'),
]
