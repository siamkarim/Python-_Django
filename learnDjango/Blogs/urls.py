from django.urls import path
from.import views
urlpatterns = [
   
    path('blog/',views.blog1,name = 'bloG'),
    path('form/',views.showFormsData),
    
]