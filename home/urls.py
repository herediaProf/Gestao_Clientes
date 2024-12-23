
from django.urls import path
from .views import home, my_logout
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', my_logout, name="logout"),
    

]
