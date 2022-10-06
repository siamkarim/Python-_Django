from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def machine(request):
    return render(request,'machine_learning/machine_learning.html')
    
def knm(request):
    return render(request,'machine_learning/knm.html')
       
def Dtree(request):
    return render(request,'machine_learning/dtree.html')
    
def rendom(request):
    return render(request,'machine_learning/rendom.html')
    