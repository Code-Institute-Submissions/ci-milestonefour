from django.test import TestCase


class ProductViewTests(TestCase):
    #
    # Product Tests
    #

    # Products Page
    def test_products_page(self):
        response = self.client.get("/products/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    # Add Product
    #def test_product_creation(self):
    #    response = self.client.post('/products/add/', {"pk": 101, "model": "products.product", "fields": {"sku": "9876", "name": "ADD PRODUCT", "description": "TEST", "has_sizes": "True", "price": 10.99, "category": 1, "subscription": "False", "rating":5, "image_url": "", "image": ""}})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/product_detail.html")

    def setUp(self):
        self.credentials = {
            'username': 'temp',
            'password': 'test'}

    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    # Product Details
    #def test_product_retrieval(self):
    #    response = self.client.get('/products/101/', follow=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/product_detail.html")

    # Edit Product
    #def test_product_change(self):
    #    response = self.client.get('/products/edit/101/', follow=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/edit_product.html")
    #    response = self.client.post('/products/edit/101/', {"pk": 101, "model": "products.product", "fields": {"sku": "9876", "name": "CHANGE PRODUCT", "description": "TEST", "has_sizes": "True", "price": 10.99, "category": 1, "subscription": "False", "rating": 5, "image_url": "", "image": ""}})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/product_detail.html")

    # Delete Product
    #def test_product_deletion(self):
    #    response = self.client.get('/products/delete/101/', follow=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/products.html")

    #
    # Subscription Tests
    #

    # Subscriptions Page
    def test_subscriptions_page(self):
        response = self.client.get("/products/subscriptions/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/subscriptions.html")

    # Add Subscription
    #def test_subscription_creation(self):
    #    response = self.client.post('/products/add/', {"pk": 102, "model": "products.product", "fields": {"sku": "6789", "name": "TEST SUBSCRIPTION", "description": "TEST", "has_sizes": "False", "price": 10.99, "category": 2, "subscription": "True", "rating": 5, "image_url": "", "image": ""}})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/subscription_detail.html")

    # Subscription Details
    #def test_subscription_retrieval(self):
    #    response = self.client.get('/products/subscriptions/102/', follow=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/subscription_detail.html")

    # Delete Subscription
    #def test_subscription_deletion(self):
    #    response = self.client.get('/products/delete/102/', follow=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, "products/subscriptions.html")
