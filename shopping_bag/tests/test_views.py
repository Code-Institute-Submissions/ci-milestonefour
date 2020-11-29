from django.test import TestCase

    #path('add/<item_id>/', views.add_to_shopping_bag, name='add_to_shopping_bag'),
    #path('update/<item_id>/', views.update_shopping_bag, name='update_shopping_bag'),
    #path('remove/<item_id>/', views.remove_from_shopping_bag, name='remove_from_shopping_bag'),

class ShoppingBagViewTests(TestCase):

    # Main Page
    def test_main_page(self):
        response = self.client.get("/shopping_bag/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shopping_bag/shopping_bag.html")

    def test_add_item_to_bag(self):
        response = self.client.get("/products/5/", follow=True)
        response = self.client.get("/shopping_bag/add/5/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    # Add New Product without login
    #def test_create_new_product(self):
    #    response = self.client.post("/products/add/", {"pk": 101, "model": "products.product", "fields": {"sku": "9876", "name": "ADD PRODUCT", "description": "TEST", "has_sizes": "True", "price": 10.99, "category": 1, "subscription": "False", "rating":5, "image_url": "", "image": ""}}, follow=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "account/login.html")
