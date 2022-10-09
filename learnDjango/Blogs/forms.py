from django import forms
from django.forms import EmailField

class TeacherRegistrations(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    Email = forms.EmailField()
