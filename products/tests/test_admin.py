from django.test import TestCase


from ..admin import ProductAdmin
from ..admin import CategoryAdmin


class AdminTests(TestCase):
    def test_product_admin(self):
        productAdmin = ProductAdmin()
        self.assertNotEqual(productAdmin.list_display, "")


class CategoryModelTests(TestCase):
    def test_category_admin(self):
        categoryAdmin = CategoryAdmin()
        self.assertNotEqual(categoryAdmin.list_display, "")
