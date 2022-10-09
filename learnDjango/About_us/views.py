from django.http import HttpResponse
from django.shortcuts import render
from About_us.models import Teacher
# Create your views here.
def about(request):
    return render (request,'about/about_us.html')

def teachers_info(request):
     teach= Teacher.objects.all()   
     return render(request,'about/t.html',{'thr': teach})  
