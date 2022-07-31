from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='user-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('flow/', views.flowchart, name='flowchart'),
    path('subpost/',views.subpost,name="post-subpost"),
    path('subpost/new/',views.createSubpost,name="subpost-create"),
    path('subpost/update/<str:pk>/',views.updateSubpost,name="subpost-update"),
    path('subpost/delete/<str:pk>',views.deleteSubpost,name="subpost-delete"),
]