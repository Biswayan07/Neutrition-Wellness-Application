from django.forms import ModelForm
from .models import *
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class addUserfood(ModelForm):
    class Meta:
        model=Userfood
        fields="__all__"
