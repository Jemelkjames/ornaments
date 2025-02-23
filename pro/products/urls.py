from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_product, name='upload_product'),
    path('', views.product_list, name='product_list'),
]