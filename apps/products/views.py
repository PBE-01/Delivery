from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.products.models import Category, Product

    # Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'index.html')




# class Products(ListView, LoginRequiredMixin):
#     model = Product
#     template_name = 'products.html'
#     context_object_name = 'products'
    
#     def get_context_data(self, **kwargs):
#         print(kwargs)
#         user = self.request.user
#         print("######u", user)
#         context = super().get_context_data(**kwargs)
        
#         print("#######", self.request.GET)
#         if self.request.GET.get('search'):
#             context['products'] = Product.objects.filter(is_active=True, name__icontains=self.request.GET.get('search'))
#         else:
#             context['products'] = Product.objects.filter(is_active=True)

#         context['user'] = user
#         context['categories'] = Category.objects.filter(is_active=True)
        
#         return context
    
class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        user = self.request.user
        print("######u", user)

        context = super().get_context_data(**kwargs)

        print("#######", self.request.GET)

        search = self.request.GET.get('search', '')
        # category = self.request.POST.get('category')

        if search:
            context['products'] = Product.objects.filter(
                is_active=True,
                # category = Category.objects.get()
                name__icontains=search,

            )
        else:
            context['products'] = Product.objects.filter(
                is_active=True
            )

        context['user'] = user
        context['categories'] = Category.objects.filter(is_active=True)
        context['search'] = search

        return context
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product-detail.html', context)