from django.urls import path

from webapp.views import CreateTaskView, DetailTaskView, DeleteTaskView, UpdateTaskView
from webapp.views.projects import ProjectsListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, \
    ProjectDeleteView

urlpatterns = [
    path('', ProjectsListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),


    path('task/<int:pk>/', DetailTaskView.as_view(), name='task_detail'),
    path('project/<int:pk>/task-add/', CreateTaskView.as_view(), name='task_add'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='task_delete'),
]

