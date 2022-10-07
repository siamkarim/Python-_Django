from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deep (request):
    return render (request,'deep_learning/deep_learnig.html')