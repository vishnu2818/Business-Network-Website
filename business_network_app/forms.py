from django import forms
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# User registration form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User login form
class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

# Company
class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyLoginForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['email', 'password']