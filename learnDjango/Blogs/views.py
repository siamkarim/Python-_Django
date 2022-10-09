from django.http import HttpResponse
from django.shortcuts import render
from .forms import TeacherRegistrations

# Create your views here.
def blog1(request):
  
    return render(request,'blog/blog.html')

def showFormsData(request):
    fm =  TeacherRegistrations()
    fm.order_fields(field_order=['Email','last_name','first_name'])
    return render(request, 'blog/form.html',{'form': fm})