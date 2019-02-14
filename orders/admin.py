from django.contrib import admin
from .models import Customer, Side, Order, SideOrder, Sauce, Crust, Topping, Pizza, PizzaTopping, PizzaOrder, PizzaToppingAlteration

# Register your models here.

admin.site.register(Customer)
admin.site.register(Side)
admin.site.register(Order)
admin.site.register(SideOrder)
admin.site.register(Sauce)
admin.site.register(Crust)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(PizzaTopping)
admin.site.register(PizzaOrder)
admin.site.register(PizzaToppingAlteration)
