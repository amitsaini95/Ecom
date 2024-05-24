from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def ProductView(request):
    products=Product.objects.all().order_by('-id')[:6]
    context={
        'products':products
    }
    return render(request,"base/productlist.html",context)
def ProductDetailView(request,slug):
    product=get_object_or_404(Product,slug=slug)
    context={'product':product}
    return render(request,"base/productDetails.html",context)
    