from django.urls import path
from.import views
urlpatterns = [
   
 
    path('deep/',views.deep,name= 'deeplar'),
    path('regis/',views.registation)
]