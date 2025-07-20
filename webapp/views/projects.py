from django.views.generic import ListView

from webapp.models import Project


class ProjectsListView(ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'projects'