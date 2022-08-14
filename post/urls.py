from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    SubPostCreateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='user-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('update/<int:pk>/', views.postUpdateView, name='post-update'),
    path('delete/<int:pk>/', views.deletePost, name='post-delete'),
    # path('flow/', views.flowchart, name='flowchart'),
    # path('subpost/',views.subpost,name="post-subpost"),

    path('post/<int:pk>/subpost/new/',SubPostCreateView.as_view(), name="subpost-create"),
    path('post/<int:pk>/subpost/<int:id>/update/',
         views.updateSubpost, name="subpost-update"),
    path('post/<int:pk>/subpost/<int:id>/delete/',
         views.deleteSubpost, name="subpost-delete"),
    #path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('search/', views.search, name='search'),

     path('post/<int:pk>/postComment/', views.postComment, name="postComment"),
     path('<int:pk>/star/', views.star, name="postStar"),
     path('stars/', views.starlist, name="stars"),
     path('categories/<slug:slug>/',views.categoryList,name='category'),

]
