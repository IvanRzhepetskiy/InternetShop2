
from django.db import models




class ProductCategory(models.Model):
    name=models.CharField(max_length=64,blank=True,default=None)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return "%s " % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    name=models.CharField(max_length=64,blank=True,default=None)
    is_active = models.TextField(default=True)
    short_description = models.TextField(blank=True, default=None, null=True)
    description = models.TextField(blank=True, default=None, null=True)
    created=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    dicsount = models.IntegerField(default=0)
    category=models.ForeignKey(ProductCategory,blank=True, null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s" % (self.price ,self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
#added Set_Null
    product = models.ForeignKey(Product, blank=True, default=None, null=True,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='products_images/')
    is_main= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'