from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=17)
    addressLine1 = models.CharField(max_length=30)
    addressLine2 = models.CharField(max_length=30)
    suburb = models.CharField(max_length=30)
    postCode = models.CharField(max_length=16)
    state = models.CharField(max_length=16)

    def __str__(self):
        return f"Name: {self.firstName} {self.lastName} Ph: {self.phoneNumber}"

class Order(models.Model):
    pass

class Side(models.Model):
    pass

class SideOrder(models.Model):
    pass

class Pizza(models.Model):
    pass

class PizzaOrder(models.Model):
    pass

class Sauce(models.Model):
    pass

class Crust(models.Model):
    pass

class Topping(models.Model):
    pass

class PizzaTopping(models.Model):
    pass

class PizzaToppingAlteration(models.Model):
    pass




