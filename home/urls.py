from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home),
    path('registration/', views.registration),
    path('login', views.login_view),
    path('home', views.home),
    
   
  
]