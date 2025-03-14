from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Category Name')
    description = models.TextField(blank=True, verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Category')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'