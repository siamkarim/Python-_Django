from django.urls import path
from.import views
urlpatterns = [
   
    path('m/',views.machine, name= 'mach'),
    path('ds/',views.Dtree,name='DT'),
    path('rm/',views.rendom,name= 'RN'),
    path('knm/',views.knm,name= 'KMN'),
   
]