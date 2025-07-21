from django import forms
from django.forms import widgets

from webapp.forms.base_form import BaseForm
from webapp.models import Task, Type, Status


class TaskForm(BaseForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all()),
    status = forms.ModelChoiceField(queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = ['description', 'detail_description', 'status', 'type']
        widgets = {
            'type' : forms.CheckboxSelectMultiple(),
        }

    def clean_detail_description(self):
        detail_description = self.cleaned_data['detail_description']
        if len(detail_description) < 10:
            raise forms.ValidationError('Подробное описание не может быть таким маленьким')
        return detail_description

    def clean(self):
        detail_description = self.cleaned_data.get('detail_description')
        description = self.cleaned_data.get('description')
        if description == detail_description:
            raise forms.ValidationError('Название и контент не могут быть одинаковыми')
        return self.cleaned_data
