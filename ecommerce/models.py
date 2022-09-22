from django.db import models

# Create your models here.

class Orders(models.Model):
    product_name = models.CharField(max_length=255, blank=True)
    product_price = models.IntegerField(blank=True)
    product_description = models.TextField(max_length=2000, blank=True)
    product_date = models.DateTimeField(auto_now_add=True)
    product_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
