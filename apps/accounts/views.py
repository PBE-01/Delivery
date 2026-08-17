from django.shortcuts import render, redirect, get_object_or_404
from apps.accounts.forms import UserForm    
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

# Create your views here.

@csrf_exempt
def login(request):
    
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            
            try:
                username_input = form.cleaned_data.get('username')
                user = User.objects.get(username=username_input)
                auth_login(request, user)
                return redirect('products:products')
            except User.DoesNotExist:
                # 3. Agar ism topilmasa, xatolik ko'rsatamiz
                messages.error(request, "Bunday foydalanuvchi topilmadi!")          
        else:
            print(form.errors)
    context = {
        "form":form
    }
    
    return render(request, 'login.html', {'form': form})