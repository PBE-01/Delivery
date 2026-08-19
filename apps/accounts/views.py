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
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            try:
                user = User.objects.get(username=username)
                if user.is_active:
                    print("######u", username)
                    print("#######", request.POST)
                    return redirect("products:products")
                else:
                    messages.error(
                        request,
                        "Sizning hisobingiz faol emas!"
                    )
            except User.DoesNotExist:
                messages.error(
                    request,
                    "Bunday username mavjud emas!"
                )
    context = {
        "form":form
    }
    return render(request, 'login.html', {'form': form})