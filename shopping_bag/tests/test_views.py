from django.test import TestCase


class ShoppingBagViewTests(TestCase):

    # Main Page
    def test_main_page(self):
        response = self.client.get("/shopping_bag/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shopping_bag/shopping_bag.html")

    def test_add_item_to_bag(self):
        response = self.client.post("/shopping_bag/add/", {'item_id': 1, 'quantity': 1, 'redirect_url': '/shopping_bag/'})
        self.assertEqual(response.status_code, 200)

    def test_update_item_in_bag(self):
        response = self.client.post("/shopping_bag/update/", {'item_id': 1, 'quantity': 2, 'redirect_url': '/shopping_bag/'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_remove_item_from_bag(self):
        response = self.client.post("/shopping_bag/remove/", {'item_id': 1}, follow=True)
        self.assertEqual(response.status_code, 200)
