from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
