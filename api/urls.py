from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import TaskApiView, TaskDetail

urlpatterns = [
    path("", TaskApiView.as_view(), name='task_list'),
    path("<int:pk>", TaskDetail.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
