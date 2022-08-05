from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    SubPostCreateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='user-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('flow/', views.flowchart, name='flowchart'),
    #path('subpost/',views.subpost,name="post-subpost"),
    path('post/<int:pk>/subpost/new/',SubPostCreateView.as_view(),name="subpost-create"),
    path('post/<int:id>/subpost/<int:pk>/update/',views.updateSubpost,name="subpost-update"),
    path('post/<int:id>/subpost/<int:pk>/delete/',views.deleteSubpost,name="subpost-delete"),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
]