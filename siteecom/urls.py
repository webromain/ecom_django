from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('templates/products/', views.product_list, name='product_list'),
    # path('nombre_de_taches', views.number_of_task, name='number_of_task'),
    path('mycart/', include('mycart.urls')),
    path('products/', include('products.urls')),
]