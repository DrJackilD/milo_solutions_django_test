from django.forms import ModelForm

from .models import CustomUserModel


class UserForm(ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'date_of_birth']


class EditUserForm(ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'first_name', 'last_name', 'date_of_birth']


class LoginForm(ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'password']
