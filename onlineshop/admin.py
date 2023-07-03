from django.contrib import admin
from .models import Category, Product, Order, TimestampModel

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "category_description", "created_at", "updated_at"]

    # def created_at(self, obj):
    #     return obj.TimestampModel.created_at

    # def updated_at(self, obj):
    #     return obj.TimestampModel.updated_at

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "description", "price", "image", "category"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["Customer_name", "customer_email", "product", "quantity"]
