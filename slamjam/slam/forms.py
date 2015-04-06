from django import forms
from django.forms import ModelForm

class SignupForm(forms.Form):
   username = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput)

