from django.shortcuts import render,HttpResponse

# Create your views here.
def IndexView(request):
    return HttpResponse("ok")