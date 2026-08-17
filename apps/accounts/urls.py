from django.urls import path
from apps.accounts.views import login

app_name = 'accounts'

urlpatterns = [
    path('', login, name='login'),
]