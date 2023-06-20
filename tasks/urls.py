from django.urls import path, include
from tasks import views

urlpatterns = [
    path('user/', views.user_tasks),
    path('<int:task_id>/', views.tasks_detail),
    path('<int:task_id>/status/', views.task_status_toggle)
]
