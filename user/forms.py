from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname','password','sex','age','icon']

    password2 = forms.CharField(max_length=128)