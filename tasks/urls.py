from django.urls import path

from . import views
from .views import TaskListCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView

urlpatterns=[
    path('home/',views.homepage,name='home'),
    path('list-create/',TaskListCreateView.as_view(),name='list_create'),
    path('update/',TaskUpdateView.as_view(),name='list_create'),
    path('delete/',TaskDeleteView.as_view(),name='list_create'),
    path('detail/',TaskDetailView.as_view(),name='list_create'),


]