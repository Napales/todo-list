from django import forms
from django.contrib.auth import get_user_model


class UsersForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all(), widget=forms.CheckboxSelectMultiple,
                                           required=False, label='Пользователь')
    class Meta:
        model = get_user_model()
        fields = ['users']