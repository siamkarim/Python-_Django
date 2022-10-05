from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deep (request):
    return HttpResponse ("this section used to deep learning")