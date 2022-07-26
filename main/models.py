from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShopList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'shoplist', null = True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Item(models.Model):
    shoplist = models.ForeignKey(ShopList, on_delete = models.CASCADE)
    name = models.CharField(max_length = 60)
    brand = models.CharField(max_length = 30, blank = True)
    quantity = models.CharField(max_length = 10, blank = True)
    unit = models.CharField(max_length = 10, blank = True)
    shop = models.CharField(max_length = 15, blank = True)
    complete = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name