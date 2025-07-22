from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import TaskForm
from webapp.models import Task, Project

class CreateTaskView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

class DeleteTaskView(DeleteView):
    model = Task

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

class DetailTaskView(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
    context_object_name = 'task'

