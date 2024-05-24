from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def ProductView(request):
    product=Product.objects.all().order_by('-id')[:6]
    context={
        'product':product
    }
    return render(request,"base/productlist.html",context)