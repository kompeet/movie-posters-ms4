from django.db import models

# Create your models here.
# Base of the models from the Boutique Ado project
# Metaclass provided to fix the spelling, 
# declare that the plural version of Category is not Categorys 


# Categories with a name and a friendly name for frontend
# Both of them have max lenght, the friendly name it's
#  not required (because blank=True)

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

# Product model with key elements
# Category, sku, image url and image fields are optional


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    year = models.IntegerField(default=2020)
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name