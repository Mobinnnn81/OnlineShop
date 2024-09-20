from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(
        max_length=500,
        default="",
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=15, default=0, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="upload/product/")

    colors = (("B", "black"), ("W", "white"), ("G", "Gray"), ("R", "red"))
    color = models.CharField(max_length=50, choices=colors, default="black")

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    addr = models.CharField(default="", max_length=250, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product
