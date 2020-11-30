from django.test import TestCase


from ..models import Order
from ..models import OrderLineItem


class CheckoutModelTests(TestCase):
    def test_checkout_order_model(self):
        order = Order(order_total=10.99)
        self.assertEqual(order.order_total, 10.99)

    def test_checkout_orderLineItem_model(self):
        orderLineItem = OrderLineItem(product_size="XL")
        self.assertEqual(orderLineItem.product_size, "XL")
