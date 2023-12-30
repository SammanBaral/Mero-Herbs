from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering =('name',)
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True, null=True)
    usage_and_benefits = models.TextField(default='', blank=False, null=False)
    price = models.CharField(max_length=255)
    quantity_available = models.CharField(max_length=255, default= "100 gm")
    image = models.ImageField(upload_to='item_images', blank=False, null=False)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        avg_rating = review.objects.filter(item=self).aggregate(avg_rating=Avg('rating'))
        return avg_rating['avg_rating'] if avg_rating['avg_rating'] else 0
    def __str__(self):
        return self.name
    




class  review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()


