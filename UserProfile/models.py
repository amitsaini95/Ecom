from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class UserProfileModel(models.Model):
    user=models.OneToOneField(User,related_name="Users",on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
