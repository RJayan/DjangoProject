from django.db import models

# Create your models here.
class Products(models.Model):
    product_upc=models.CharField(max_length=20,default='not given')
    product_name=models.CharField(max_length=30)
    product_stock=models.IntegerField(default=0)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return(self.product_name)
    class Meta:
        verbose_name_plural="Products"

class Store(models.Model):
    store_name=models.CharField(max_length=20,default='not given')
    store_code=models.IntegerField(default=0)

    def __str__(self):
        return(self.store_name)
    class Meta:
        verbose_name_plural = "Store"    


