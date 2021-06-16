from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('food/<str:id>', views.food, name='food')
]
