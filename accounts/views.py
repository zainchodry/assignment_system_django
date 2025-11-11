from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from django.contrib.auth import logout as auth_logout



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account were created Successfully")
            return redirect('login')
    form = RegisterForm()
    return render(request, "register.html", {"form":form})


def logout(request):
    auth_logout(request)
    messages.success(request, "You Logout Successfully")
    return redirect('login')
