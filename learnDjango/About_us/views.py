from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    return HttpResponse ("about section")