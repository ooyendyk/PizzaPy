from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User, Customer, Side, Order, SideOrder, Sauce, Crust, Topping, Pizza, PizzaTopping, PizzaOrder, PizzaToppingAlteration

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline, )

# Re-register UserAdmin


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
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
