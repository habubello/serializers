from django.contrib.auth.models import User
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
    likes = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'





class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/", verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"Image for {self.product.name}"



class Comment(models.Model):
    content = models.TextField(),
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment_user')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_comment')
    created_at = models.DateTimeField()
    rating = models.SmallIntegerField()
    image = models.FileField(upload_to="comment_images")

