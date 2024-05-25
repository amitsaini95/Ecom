from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
# Create your views here.
def SignUpView(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user_data=form.save()
            user=UserProfileModel.objects.create(user=user_data)
            return redirect('/')
    else:
        form=UserCreationForm()
    context={
        'form':form
    }
    return render(request,"base/signup.html",context)