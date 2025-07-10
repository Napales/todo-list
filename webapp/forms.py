from django import forms
from django.forms import widgets

from webapp.models import Task


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = ['description', 'status', 'complete_date', 'detail_description']
        widgets = {
            "complete_date": widgets.DateInput(attrs={'type': 'date'})
        }