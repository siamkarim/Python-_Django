from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data(request):
    return render (request,'data_analysis/data_analysis.html')