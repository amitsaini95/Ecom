from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def ProductView(request):
    cat=request.GET.get('category')  if request.GET.get('category') != None else ''
    categories=Category.objects.all()
    products=Product.objects.filter(category__slug__icontains=cat)
    print(products)
    context={
            'products':products,
            'categories':categories
    }
    return render(request,"base/productlist.html",context)
    
def ProductDetailView(request,slug):
    product=get_object_or_404(Product,slug=slug)
    context={'product':product}
    return render(request,"base/productDetails.html",context)
def CategoryView(request):
    category=Category.objects.all()
    context={
        'categories':category
    }
    return render(request,"base/category.html",context)

    