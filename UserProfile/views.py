from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignUpForm
from .models import *
# Create your views here.
def SignUpView(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user_data=form.save()
            user=UserProfileModel.objects.create(user=user_data)
            return redirect('auth:Login')
    else:
        form=SignUpForm()
    context={
        'form':form
    }
    return render(request,"base/signup.html",context)
def LoginView(request):
    if request.method == "POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is  not None:
                login(request,user)
                return redirect('product:ProductList')         
    else:
        form=LoginForm()
    context={
        'form':form
    }
    return render(request,"base/login.html",context)
def LogoutView(request):
    logout(request)
    return redirect('auth:Login')
            