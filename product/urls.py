from django.urls import path
from .import views
app_name="product"
urlpatterns=[
    path('',views.ProductView,name="ProductList"), 
    path('category',views.CategoryView,name="Categorylist"),
    path('product/<slug:slug>',views.ProductDetailView,name="productDetails") ,
    path('addProduct',views.AddProductView,name="Addproductlist"),
    path('edit/product/<slug:slug>',views.EditProductView,name="editproductlist"),

]