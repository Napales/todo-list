from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm
from webapp.forms.projects import ProjectForm
from webapp.models import Project


class ProjectsListView(ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 5
    ordering = ['id']

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs ):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result['query'] = urlencode({'search': self.search_value})
            result['search'] = self.search_value
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']




class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/project_detail.html'
    model = Project
    context_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    model = Project


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/project_delete.html'
    model = Project
    success_url = reverse_lazy('webapp:project_list')


