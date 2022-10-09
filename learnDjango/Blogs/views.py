from django.http import HttpResponse
from django.shortcuts import render
from .forms import TeacherRegistrations

# Create your views here.
def blog1(request):
  
    return render(request,'blog/blog.html')

def showFormsData(request):
    if request.method == 'POST':
      fm =  TeacherRegistrations(request.POST)
      if fm.is_valid():
       print(fm.cleaned_data['password'])
       print(fm.cleaned_data['repassword'])
      
      
 
    else:
        fm =  TeacherRegistrations()
        print('this is get statement')

   
    return render(request, 'blog/form.html',{'form': fm})