from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('avatar', views.UpdateAvatarView.as_view(), name='update_avatar'),
    path('follow', views.FollowView.as_view(), name='follow_user'),
]
