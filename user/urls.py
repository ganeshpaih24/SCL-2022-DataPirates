from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='user-login-home'),
    path('about/', views.login_about, name='user-login-about'),
]
