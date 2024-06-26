from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import ProductForm
# Create your views here.
def ProductView(request):
    cat=request.GET.get('category')  if request.GET.get('category') != None else ''
    categories=Category.objects.all()
    products=Product.objects.filter(category__slug__icontains=cat)
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
def AddProductView(request):
    if request.method == "POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProductForm()
    context={
        'form':form
    }
    return render(request,"base/addproduct.html",context)
def EditProductView(request,slug):
    instance=get_object_or_404(Product,slug=slug)
    if request.method == "POST":
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProductForm(instance=instance)
    context={
        'form':form
    }
    return render(request,"base/editproduct.html",context)
def AddCartView(request):

    product_id=request.POST.get('product-id') if request.POST.get('product-id') !=None else ''
    product=get_object_or_404(Product,id=product_id)
    print(product)
    cartitem=Cart.objects.filter(product=product,user=request.user)
    for cart in cartitem:
        cart.quantity +=1
        cart.save()
        return redirect('product:cartViewlist')
    if not cartitem:
        cartitem=Cart.objects.create(product=product,user=request.user)
        cartitem.quantity=1
        cartitem.save()
        return redirect('product:cartViewlist')
  
def CartViewList(request):
    cartdata=Cart.objects.filter(user=request.user)
    totalitem=cartdata.count()
    totalprice=sum(item.product.price *item.quantity for item in cartdata)
    context={
        'cart':cartdata, 
        'productcost':totalprice,
        'totalitem':totalitem  
    }
    return render(request,"base/cart.html",context)
def CheckoutView(request):
    pass

def DeleteProductView(request,id):
    productDel=get_object_or_404(Cart,id=id)
    productDel.delete()

    return redirect('product:cartViewlist')