from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_home, name='user-login-home'),
    path('about/', views.login_about, name='user-login-about'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

]