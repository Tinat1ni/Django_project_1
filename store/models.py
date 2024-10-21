from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                                    related_name='children', blank=True, null=True)
    slug = models.SlugField(unique=True, default='default-slug')

    def __str__(self):
        return self.name

def default_additional_information():
    return {'Weight': None,
            'Country of Origin': None,
            'Quality': None,
            'Check': None,
            'Min Weight': None}


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    organic = models.BooleanField(default=False)
    fresh = models.BooleanField(default=False)
    sales = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    additional_information = models.JSONField(default = default_additional_information)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name