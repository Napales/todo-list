from django.urls import path

from webapp.views import IndexTaskView, CreateTaskView, DetailTaskView, DeleteTaskView, UpdateTaskView
from webapp.views.projects import ProjectsListView, ProjectDetailView

urlpatterns = [
    path('', ProjectsListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),


    path('task/list', IndexTaskView.as_view(), name='index'),
    path('task/<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
    path('add-task/', CreateTaskView.as_view(), name='add-task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]

