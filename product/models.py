from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(blank=True,max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"