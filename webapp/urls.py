from django.urls import path

from webapp.views import index, create_task, detail_task, update_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('add-task/', create_task, name='add-task'),
    path('task/<int:pk>/', detail_task, name='detail_task'),
    path('task/<int:pk>/update/', update_task, name='update_task'),
    path('task/<int:pk>/delete/', delete_task, name='delete_task'),
]

