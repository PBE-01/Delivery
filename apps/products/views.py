from django.shortcuts import render, get_object_or_404

from apps.products.models import Category, Product

    # Create your views here.

def home(request):
    return render(request, 'index.html')
