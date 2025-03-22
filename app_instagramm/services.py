from django.core.cache import cache
from django.db import models

class ProductManager(models.Manager):
    def get_cached_products(self):
        key = 'products'  # Уникальный ключ для кэша
        products = cache.get(key)

        if not products:  # Если данных нет в кэше, получаем их из базы
            products = self.get_queryset().select_related('category').prefetch_related('likes').all()
            cache.set(key, products, timeout=60 * 15)  # Кэшируем на 15 минут

        return products

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='Category')
    likes = models.ManyToManyField('User', blank=True)

    objects = ProductManager()  # Назначаем кастомный менеджер

