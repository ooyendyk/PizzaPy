from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Side, sauce, crust and topping all have identical attributes.
# Maybe it would be best to have them inherit from a common parent class?


class Customer(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=48)
    lastName = models.CharField(max_length=48)
    phoneNumber = models.CharField(max_length=24)
    addressLine1 = models.CharField(max_length=32)
    addressLine2 = models.CharField(max_length=32)
    suburb = models.CharField(max_length=32)
    postCode = models.CharField(max_length=16)
    state = models.CharField(max_length=16)

    def __str__(self):
        return f"Name: {self.firstName} {self.lastName} Ph: {self.phoneNumber}"


class Side(models.Model):
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"


class Sauce(models.Model):
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"


class Crust(models.Model):
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"


class Topping(models.Model):
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"


class Pizza(models.Model):
    sauceID = models.ForeignKey(Sauce, on_delete=models.CASCADE)  # Might need '()' on .CASCADE
    crustID = models.ForeignKey(Crust, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, through='PizzaTopping')
    name = models.CharField(max_length=16)
    priceModifier = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} Sauce: {self.sauceID} Crust: {self.crustID} Toppings: {self.toppings} Price: {self.priceModifier}"


class Order(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, through='PizzaOrder')
    sides = models.ManyToManyField(Side, through='SideOrder')
    orderDateTime = models.DateTimeField(default=datetime.now, blank=True)
    orderStatus = models.CharField(default="Pending", max_length=16)

    def __str__(self):
        return f"Customer: {self.customerID} Status: {self.orderStatus} Sides: {self.sides}"


class SideOrder(models.Model):
    sideID = models.ForeignKey(Side, on_delete=models.CASCADE)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MaxValueValidator(512)])

    def __str__(self):
        return f"Side: {self.sideID} Order: {self.orderID} Quantity: {self.quantity}"


class PizzaTopping(models.Model):
    pizzaID = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    toppingID = models.ForeignKey(Topping, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MaxValueValidator(3)])

    def __str__(self):
        return f"Pizza: {self.pizzaID} Topping: {self.toppingID} Quantity: {self.quantity}"


class PizzaOrder(models.Model):
    pizzaID = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    sauceIDAlteration = models.ForeignKey(Sauce, on_delete=models.CASCADE, null=True, blank=True)
    crustIDAlteration = models.ForeignKey(Crust, on_delete=models.CASCADE, null=True, blank=True)
    toppings = models.ManyToManyField(Topping, through='PizzaToppingAlteration')
    quantity = models.IntegerField(validators=[MaxValueValidator(512)])

    def __str__(self):
        return f"Pizza: {self.pizzaID} Order: {self.orderID} Sauce_Alteration: {self.sauceIDAlteration} Crust_Alteration: {self.crustIDAlteration} Toppings: {self.toppings} Quantity: {self.quantity}"


class PizzaToppingAlteration(models.Model):
    pizzaOrderID = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE)
    toppingID = models.ForeignKey(Topping, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MaxValueValidator(3)])

    def __str__(self):
        return f"Pizza Order: {self.pizzaOrderID} Topping: {self.toppingID} Quantity {self.quantity}"
