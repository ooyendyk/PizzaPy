from django.test import TestCase
from .models import Customer, Side, Order, SideOrder, Sauce, Crust, Topping, Pizza, PizzaTopping, PizzaOrder, PizzaToppingAlteration

# Create your tests here.


class CustomerModelTest(TestCase):
    def test_string_representation(self):
        customer = Customer(firstName="John", lastName="Doe", phoneNumber="+61-234-567-890",
                            addressLine1="10 Example St", addressLine2="Apt 20", suburb="Sydney", postCode="1000",
                            state="NSW")
        self.assertEqual(str(customer), "Name: John Doe Ph: +61-234-567-890")


class SideModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class OrderModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class SideOrderModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class SauceModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class CrustModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class ToppingModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class PizzaModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class PizzaToppingModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class PizzaOrderModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")


class PizzaToppingAlterationModelTest(TestCase):
    def test_string_representation(self):
        self.fail("TODO Test incomplete")
