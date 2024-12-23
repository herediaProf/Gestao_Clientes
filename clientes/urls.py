
from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from . import views

urlpatterns = [
    path('list/', views.persons_list, name="persons_list"),
    path('new/', views.persons_new, name="persons_new"),
    path('update/<int:id>', views.persons_update, name="persons_update"),
    path('delete/<int:id>', views.persons_delete, name="persons_delete")
   
] 
