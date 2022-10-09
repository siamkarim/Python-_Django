from django.urls import path
from.import views
urlpatterns = [
   
    path('abt/',views.about, name='ab'),
    path('t/',views.teachers_info),
]