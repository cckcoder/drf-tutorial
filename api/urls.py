from django.urls import path
from .views import TaskApiView

urlpatterns = [
    path("", TaskApiView.as_view(), name='task_list')
]
