from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm
from webapp.forms.projects import ProjectForm
from webapp.forms.users_project import UsersForm
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




class ProjectDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'projects/project_detail.html'
    model = Project
    context_object_name = 'project'
    permission_required = 'webapp.view_project'

    def has_permission(self):
        return super().has_permission() and self.get_object().user.filter(pk=self.request.user.pk).exists()



class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:project_list')
    permission_required = 'webapp.add_project'

    def has_permission(self):
        return super().has_permission()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.change_project'

    def has_permission(self):
        return super().has_permission() and self.get_object().user.filter(pk=self.request.user.pk).exists()


# self.request.user in self.get_object().project.user.all()


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'projects/project_delete.html'
    model = Project
    success_url = reverse_lazy('webapp:project_list')
    permission_required = 'webapp.delete_project'

    def has_permission(self):
        return super().has_permission() and self.get_object().user.filter(pk=self.request.user.pk).exists()


class UsersProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'projects/users_project.html'
    model = Project
    form_class = UsersForm
    permission_required = 'webapp.change_project'

    def has_permission(self):
        return super().has_permission() and self.get_object().user.filter(pk=self.request.user.pk).exists()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.object:
            kwargs['initial'] = {'users': self.object.user.all()}
        return kwargs

    def form_valid(self, form):
        project = self.get_object()
        users = form.cleaned_data.get('users')
        project.user.set(users)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:project_detail', kwargs={'pk': self.object.pk})


