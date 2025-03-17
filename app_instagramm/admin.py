from django.contrib import admin
from app_instagramm.models import Product , ProductImage,Category,Comment
# Register your models here.

admin.site.register(Category)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    inlines = [ProductImageInline]

admin.site.register(ProductImage)
admin.site.register(Comment)