from django.urls import path


from apps.products.views import home


app_name = 'products' 


urlpatterns = [
    path('', home, name='home'),
]