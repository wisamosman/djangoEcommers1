from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _


FLAG_TYPES = (
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(_('name'),max_length=120)
    description = models.TextField(max_length=30000)
    sku = models.IntegerField()
    price = models.FloatField()
    subtitle = models.TextField(max_length=600)
    image = models.ImageField(upload_to='products')
    brand = models.ForeignKey('Brand' , verbose_name=_('brand'), on_delete=models.CASCADE , related_name='product_brand')
    flag = models.CharField(max_length=20 , choices=FLAG_TYPES)
    tags = TaggableManager()



    def __str__(self):
        return f"(self.name) - (self.price)"   



class ProductImages(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product , related_name='product_images' , on_delete=models.CASCADE)




class Brand(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    

    def __str__(self):
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,null=True,blank=True , related_name='user_review')
    product = models.ForeignKey(Product , related_name='product_review' , on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    create_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"(self.user) - (self.product)"    

