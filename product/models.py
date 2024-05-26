from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(blank=True,max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        return super(Category,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"
class Tag(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(blank=True,max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        return super(Tag,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Tags"
class Product(models.Model):
    name=models.CharField(max_length=60)
    slug=models.CharField(blank=True,max_length=60)
    auth=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name="category")
    productImage=models.ImageField(upload_to="productImage",null=True,blank=True)
    tag=models.ManyToManyField(Tag,null=True,blank=True)
    desc=models.TextField()
    price=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        return super(Product,self).save(*args,**kwargs)
    
    def productimage(self):
        try:
            url=self.productImage.url
        except:
            url=''
        return url
    
    def __str__(self):
        return self.name
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.PositiveIntegerField(null=True,default=1)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product.name
    def totalPrice(self):
        return self.product.price *self.quantity

    
    