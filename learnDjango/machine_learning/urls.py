from django.urls import path
from.import views
urlpatterns = [
   
    path('',views.machine),
    path('dl/',views.deep),
]