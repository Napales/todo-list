from django import forms
from django.forms import widgets

from webapp.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = ['description', 'detail_description', 'status', 'type']