from django import forms
from webapp.forms.base_form import BaseForm
from webapp.models import Project


class ProjectForm(BaseForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date' : forms.DateInput(attrs={'type': 'date'}),
            'end_date' : forms.DateInput(attrs={'type': 'date'}),
        }
