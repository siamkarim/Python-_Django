
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def deep (request):
    return render (request,'deep_learning/deep_learnig.html')


def registation (request):
    if request.method == "POST":
      fm = UserCreationForm(request.POST)
      if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()        
    return render (request,'deep_learning/register.html',{'form':fm})   