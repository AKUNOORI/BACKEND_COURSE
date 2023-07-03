from django.db import models

# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Category(TimestampModel):
    category_name = models.CharField(max_length = 200)
    category_description = models.CharField(max_length = 350)

    def __str__(self):
        return self.category_name
    
class Product(TimestampModel):
    product_name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 300)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.FileField(upload_to = 'products/')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.product_name
    
class Order(TimestampModel):
    Customer_name = models.CharField(max_length = 200)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return f"oder # {self.id}"
