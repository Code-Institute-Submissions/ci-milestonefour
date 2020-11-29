from django.test import TestCase


from ..models import Product
from ..models import Category


class ProductModelTests(TestCase):
    def test_product_model(self):
        product = Product(name="Test product", subscription=False)
        self.assertEqual(product.name, "Test product")


class CategoryModelTests(TestCase):
    def test_category_model(self):
        category = Category(name="Test category", friendly_name="Friendly category name")
        self.assertEqual(category.friendly_name, "Friendly category name")
