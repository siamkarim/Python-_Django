from django.urls import path
from.import views
urlpatterns = [
   
    path('data/',views.data,name='dataana'),
    path('class/',views.DataAnalysis.as_view()),
]