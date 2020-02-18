from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('me/avatar', views.UpdateAvatarView.as_view(), name='update_avatar'),
    path('me/follow', views.FollowView.as_view(), name='follow_user'),
]
