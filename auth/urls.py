from django.urls import path
from . import views


app_name = 'auth'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('reset_password', views.ResetPasswordView.as_view(), name='reset_password'),
    path('renew_auth', views.RenewAuthTokenView.as_view(), name='renew_auth'),
    path('renew_refresh', views.RenewRefreshTokenView.as_view(), name='renew_refresh'),

    path('avatar', views.UpdateAvatarView.as_view(), name='update_avatar'),
]
