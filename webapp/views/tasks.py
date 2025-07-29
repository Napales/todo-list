from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import TaskForm
from webapp.models import Task, Project

class CreateTaskView(PermissionRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    permission_required = 'webapp.add_task'

    def has_permission(self):
        return super().has_permission() and self.get_object().project.user.filter(pk=self.request.user.pk).exists()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})

class UpdateTaskView(PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    permission_required = 'webapp.change_task'

    def has_permission(self):
        return super().has_permission() and self.get_object().project.user.filter(pk=self.request.user.pk).exists()

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})

class DeleteTaskView(PermissionRequiredMixin, DeleteView):
    model = Task
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        return super().has_permission() and self.get_object().project.user.filter(pk=self.request.user.pk).exists()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})

class DetailTaskView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
    context_object_name = 'task'
    permision_required = 'webapp.view_task'

    def has_permission(self):
        return super().has_permission() and self.get_object().project.user.filter(pk=self.request.user.pk).exists()


