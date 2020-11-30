from django.test import TestCase


class CheckoutViewTests(TestCase):

    # Checkout Page
    def test_main_checkout_page(self):
        response = self.client.get("/checkout/", follow=True)
        self.assertEqual(response.status_code, 200)

    # Checkout Page
    def test_checkout_success_page_fails_with_fake_order(self):
        response = self.client.get("/checkout_success/12345", follow=True)
        self.assertEqual(response.status_code, 404)
