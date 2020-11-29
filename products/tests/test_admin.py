from django.test import TestCase
from django.contrib import admin

from ..models import Product, Category
from ..admin import ProductAdmin
from ..admin import CategoryAdmin


class AdminTests(TestCase):
    def test_product_admin(self):
        productAdmin = ProductAdmin(Product(), admin.ModelAdmin)
        self.assertNotEqual(productAdmin.list_display, "")


class CategoryModelTests(TestCase):
    def test_category_admin(self):
        categoryAdmin = CategoryAdmin(Category(), admin.ModelAdmin)
        self.assertNotEqual(categoryAdmin.list_display, "")
