from django.urls import path
from . import views

urlpatterns = [
    path('chickens/', views.chicken_list, name='chicken_list'),
    path('chickens/add/', views.chicken_add, name='chicken_add'),
    path('chickens/edit/<int:pk>/', views.chicken_edit, name='chicken_edit'),
    path('chickens/delete/<int:pk>/', views.chicken_delete, name='chicken_delete'),
    path('eggs/', views.egg_list, name='egg_list'),
    path('eggs/add/<int:chicken_id>/', views.egg_add, name='egg_add'),
   
]
