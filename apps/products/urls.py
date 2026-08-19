from django.urls import path

from apps.products.views import Home, Products, ProductDetailView


app_name = 'products' 

urlpatterns = [
    # path('', home, name='home'),
    path('', Home.as_view(), name='home'),
    
    # path('products/', product, name='products'),
    
    path('products/', Products.as_view(), name='products'),
    
    # path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]