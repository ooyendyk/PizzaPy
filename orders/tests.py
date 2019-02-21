from django.test import TestCase
from .models import User, Customer, Side, Order, SideOrder, Sauce, Crust, Topping, Pizza, PizzaTopping, PizzaOrder, \
    PizzaToppingAlteration

# TODO: Fix obscenely long strings
# TODO: Setup DB init function/object for code reuse


class CustomerModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create_user(username="johnD", password="welcome")
        customer = Customer.objects.create(userID=user, firstName="Kingsford", lastName="Smith",
                                           phoneNumber="+61-234-567-890", addressLine1="10 Example St",
                                           addressLine2="Apt 20", suburb="Sydney", postCode="2000", state="NSW")
        self.assertEqual(str(customer), "Name: Kingsford Smith Ph: +61-234-567-890")


class SideModelTest(TestCase):
    def test_string_representation(self):
        side = Side.objects.create(name="Garlic Bread", price=4.00)
        self.assertEqual(str(side), "Name: Garlic Bread Price: 4.0")


class SauceModelTest(TestCase):
    def test_string_representation(self):
        sauce = Sauce.objects.create(name="Classic Tomato", price=0.00)
        self.assertEqual(str(sauce), "Name: Classic Tomato Price: 0.0")


class CrustModelTest(TestCase):
    def test_string_representation(self):
        crust = Crust.objects.create(name="Deep Pan", price=8.00)
        self.assertEqual(str(crust), "Name: Deep Pan Price: 8.0")


class ToppingModelTest(TestCase):
    def test_string_representation(self):
        topping = Topping.objects.create(name="Prosciutto", price=3.00)
        self.assertEqual(str(topping), "Name: Prosciutto Price: 3.0")


class PizzaModelTest(TestCase):
    def test_string_representation(self):
        crust = Crust.objects.create(name="Deep Pan", price=8.00)
        sauce = Sauce.objects.create(name="Classic Tomato", price=0.00)
        pizza = Pizza.objects.create(sauceID=sauce, crustID=crust, name="Plain", priceModifier=0.00)
        self.assertEqual(str(pizza), "Name: Plain Sauce: Name: Classic Tomato Price: 0.0 Crust: Name: Deep Pan Price: 8.0 Toppings: orders.Topping.None Price: 0.0")


class PizzaToppingModelTest(TestCase):
    def test_string_representation(self):
        crust = Crust.objects.create(name="Deep Pan", price=8.00)
        sauce = Sauce.objects.create(name="Classic Tomato", price=0.00)
        pizza = Pizza.objects.create(sauceID=sauce, crustID=crust, name="Plain", priceModifier=0.00)
        topping = Topping.objects.create(name="Prosciutto", price=3.00)
        pizza_topping = PizzaTopping.objects.create(pizzaID=pizza, toppingID=topping, quantity=1)
        self.assertEqual(str(pizza_topping), "Pizza: Name: Plain Sauce: Name: Classic Tomato Price: 0.0 Crust: Name: Deep Pan Price: 8.0 Toppings: orders.Topping.None Price: 0.0 Topping: Name: Prosciutto Price: 3.0 Quantity: 1")


class OrderModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create_user(username="johnD", password="welcome")
        customer = Customer.objects.create(userID=user, firstName="Kingsford", lastName="Smith",
                                           phoneNumber="+61-234-567-890", addressLine1="10 Example St",
                                           addressLine2="Apt 20", suburb="Sydney", postCode="2000", state="NSW")
        order = Order.objects.create(customerID=customer)
        self.assertEqual(str(order), f"Customer: Name: Kingsford Smith Ph: +61-234-567-890 Status: Pending Sides: orders.Side.None")


class SideOrderModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create_user(username="johnD", password="welcome")
        customer = Customer.objects.create(userID=user, firstName="Henry", lastName="Lawson",
                                           phoneNumber="+61-987-654-321", addressLine1="437 Great North Rd",
                                           addressLine2="Unit 1", suburb="Abbotsford", postCode="2046", state="NSW")
        order = Order.objects.create(customerID=customer)
        side = Side.objects.create(name="Garlic Bread", price=4.00)
        side_order = SideOrder.objects.create(sideID=side, orderID=order, quantity=1)
        self.assertEqual(str(side_order), f"Side: Name: Garlic Bread Price: 4.0 Order: Customer: Name: Henry Lawson Ph: +61-987-654-321 Status: Pending Sides: orders.Side.None Quantity: 1")


class PizzaOrderModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create_user(username="johnD", password="welcome")
        customer = Customer.objects.create(userID=user, firstName="Banjo", lastName="Paterson",
                                           addressLine1="1 Punt Rd", addressLine2="Banjo Paterson Park",
                                           suburb="Gladesville", postCode="2111", state="NSW")
        order = Order.objects.create(customerID=customer)
        crust = Crust.objects.create(name="Deep Pan", price=8.00)
        sauce = Sauce.objects.create(name="Classic Tomato", price=0.00)
        sauce2 = Sauce.objects.create(name="Smokey Barbecue", price=0.00)
        crust2 = Crust.objects.create(name="Cheesy Crust", price=12.00)
        pizza = Pizza.objects.create(sauceID=sauce, crustID=crust, name="Plain", priceModifier=0.00)
        pizza_order = PizzaOrder.objects.create(pizzaID=pizza, orderID=order, sauceIDAlteration=sauce2,
                                                crustIDAlteration=crust2, quantity=2)
        self.assertEqual(str(pizza_order), f"Pizza: Name: Plain Sauce: Name: Classic Tomato Price: 0.0 Crust: Name: Deep Pan Price: 8.0 Toppings: orders.Topping.None Price: 0.0 Order: Customer: Name: Banjo Paterson Ph: 02 9555 3611 Status: Pending Sides: orders.Side.None Sauce_Alteration: Name: Smokey Barbecue Price: 0.0 Crust_Alteration: Name: Cheesy Crust Price: 12.0 Toppings: orders.Topping.None Quantity: 2")


class PizzaToppingAlterationModelTest(TestCase):
    def test_string_representation(self):
        user = User.objects.create_user(username="johnD", password="welcome")
        customer = Customer.objects.create(userID=user, firstName="Caroline", lastName="Chisholm",
                                           phoneNumber="0405555555", addressLine1="86 George St",
                                           addressLine2="Unit B", suburb="Windsor", postCode="2756", state="NSW")
        order = Order.objects.create(customerID=customer)
        crust = Crust.objects.create(name="Deep Pan", price=8.00)
        sauce = Sauce.objects.create(name="Classic Tomato", price=0.00)
        pizza = Pizza.objects.create(sauceID=sauce, crustID=crust, name="Plain", priceModifier=0.00)
        topping = Topping.objects.create(name="Mozzarella", price=1.00)
        pizza_order = PizzaOrder.objects.create(pizzaID=pizza, orderID=order, quantity=1)
        pizza_topping_alteration = PizzaToppingAlteration.objects.create(pizzaOrderID=pizza_order, toppingID=topping,
                                                                         quantity=1)
        self.assertEqual(str(pizza_topping_alteration), f"Pizza Order: Pizza: Name: Plain Sauce: Name: Classic Tomato Price: 0.0 Crust: Name: Deep Pan Price: 8.0 Toppings: orders.Topping.None Price: 0.0 Order: Customer: Name: Caroline Chisholm Ph: 0405555555 Status: Pending Sides: orders.Side.None Sauce_Alteration: None Crust_Alteration: None Toppings: orders.Topping.None Quantity: 1 Topping: Name: Mozzarella Price: 1.0 Quantity 1")  # Wow thats bad!
