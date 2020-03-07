from __future__ import unicode_literals
from django.db import models
from datetime import date

class Restaurant_Validator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['name'] == "":
            errors['name'] = "Name Field is required"
        if postData['yourphone'] == "":
            errors['yourphone'] = "Number Field is required"
        if postData['date'] == "":
            errors["date"] = "Date Field is required"
        return errors

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    date = models.DateField()
    code = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    objects = Restaurant_Validator()

class Product_Validator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['name'] == "":
            errors['name'] = "Name Field is required"
        if postData['quantity'] == "":
            errors['quantity'] = "Quantity Field is required"
        return errors

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    objects = Product_Validator()

class Setup(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="setup")
    product = models.ForeignKey(Product, related_name='setup')
    price = models.CharField(max_length=255)

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="orders")
    product = models.ForeignKey(Product, related_name="orders")
    order_number = models.IntegerField()