from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('nombre_de_taches', views.number_of_task, name='number_of_task'),
]