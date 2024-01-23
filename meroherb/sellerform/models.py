from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SellerAccount(models.Model):
    user1=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    location=models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.user.username
    