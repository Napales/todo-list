from django.urls import path

from webapp.views import IndexView, CreateView, DetailView, DeleteView, UpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', DetailView.as_view(), name='detail_task'),
    path('add-task/', CreateView.as_view(), name='add-task'),
    path('task/<int:pk>/update/', UpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteView.as_view(), name='delete_task'),
]

