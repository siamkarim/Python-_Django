from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog1(request):
    siam ="This is blog section ,we are working here"
    fil = {'var':siam}
    return render(request,'blog/blog.html',context = fil)