from django.shortcuts import HttpResponse, render

# Create your views here.
def machine(request):
    return HttpResponse("this is first step for machine learning");
    
def deep(request):
  return HttpResponse(" deep learning start")   

