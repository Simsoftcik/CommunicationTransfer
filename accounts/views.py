
from django.shortcuts import render, redirect
from .forms import CreateUserForm, Account
from .models import Accounts

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_user

@login_required(login_url='login')
def profile(request):
    user = request.user
    data = Accounts.objects.filter(user=user).first()
    form = Account(instance=data)
    print(request.method)
    if request.method == 'POST':
        form = Account(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'data':data}
    return render(request, 'profile.html', context)

def register(response):
    if response.method == 'POST':
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = CreateUserForm()

    return render(response, 'registration/register.html', {'form': form})

def logout(request):
    logout_user(request)
    return redirect('/')