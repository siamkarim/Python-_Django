from django import forms
from django.core import validators

class TeacherRegistrations(forms.Form):
    first_name = forms.CharField(label='Enter Your First Name',label_suffix=' ')
    last_name = forms.CharField( initial='Hossain')
    Email = forms.EmailField(initial='siam@gmail.com', disabled=True )
    password = forms.CharField(widget= forms.PasswordInput)
    repassword = forms.CharField(widget= forms.PasswordInput)
    Textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput )
    
    def clean(self):
        cleaned_data = super().clean()
        rightpassword = self.cleaned_data['password']
        wrongpassword = self.cleaned_data['repassword']
        if rightpassword != wrongpassword:
            raise forms.ValidationError('password does not match')