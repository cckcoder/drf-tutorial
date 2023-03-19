from django.urls import path
from .views import TaskApiView, TaskDetail

urlpatterns = [
    path("", TaskApiView.as_view(), name='task_list'),
    path("<int:pk>", TaskDetail.as_view())
]
