from django.urls import path
from . import views


app_name = 'auth'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('reset_password', views.ResetPasswordView.as_view(), name='reset_password'),
    path('token/refresh', views.RefreshTokenView.as_view(), name='refresh_token'),
]
