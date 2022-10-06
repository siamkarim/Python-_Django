from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def machine(request):
    time = 28
    name = "siam"
    progam = "BCSE"
    learn = { 'age':time,'nm':name,'pr':progam}
    return render(request,'machine_learning/machine_learning.html', context=learn)
    
def knm(request):
    return render(request,'machine_learning/knm.html')
       
def Dtree(request):
    return render(request,'machine_learning/dtree.html')
    
def rendom(request):
    return render(request,'machine_learning/rendom.html')
    