# store/models.py

from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')  # Category image

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Retailer Model
class Retailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User
    shop_name = models.CharField(max_length=255)
    shop_image = models.ImageField(upload_to='shop_images/', blank=True, null=True)

    def __str__(self):
        return self.shop_name

# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User who placed the order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the ordered Product
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} by {self.user.username}"

# Cart Model (Optional)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User who owns the cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart - {self.user.username} - {self.product.name}"
