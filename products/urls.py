from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register_, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('profil/', views.profil, name='profil')
] 