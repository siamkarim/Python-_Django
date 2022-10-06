from django.urls import path
from.import views
urlpatterns = [
   
    path('m/',views.machine),
    path('ds/',views.Dtree),
    path('rm/',views.rendom),
    path('knm/',views.knm),
   
]