from django.test import TestCase
from .models import Queue, Customer, Order
from .services import QueueService, OrderCancelError, SwapError
# Create your tests here.


def create_order(customer, details, store):
    return Order.objects.create(customer=customer, details=details, queue_id=store)


def create_queue(store):
    return Queue.objects.create(store_name=store)


def create_customer(username):
    return Customer.objects.create(username=username)


def fill_queue(size, start=3):
    for id in range(start,size+start):
        customer = create_customer(id)
        order = create_order(customer, 'pizza', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order)


class ServicesMethodTests(TestCase):

    def setUp(self):
        create_queue("One")
        create_customer("1")
        create_customer("2")

    def test_order_placed_on_empty_queue(self):
        customer = Customer.objects.get(pk='1')
        order = create_order(customer, 'pizza', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order)
        self.assertEqual(order.priority, 1)
        self.assertEqual(qs.get_size(), 1)

    def test_order_placed_on_one(self):
        customer1 = Customer.objects.get(username='1')
        order1 = create_order(customer1, 'pizza', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order1)
        customer2 = Customer.objects.get(username='2')
        order2 = create_order(customer2, 'more pizze', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order2)
        self.assertEqual(order2.priority, 2)
        self.assertEqual(qs.get_size(), 2)

    def test_cancel_order_when_order_exists(self):
        customer = Customer.objects.get(pk='1')
        order = create_order(customer, 'pizza', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order)
        self.assertEqual(order.cancelled, False)
        self.assertEqual(order.priority, 1)
        qs.cancel_order(order)
        self.assertEqual(order.cancelled, True)
        self.assertEqual(qs.get_size(), 0)

    def test_cancel_order_on_large_queue(self):
        qs = QueueService(Queue.objects.get(store_name='One').id)
        fill_queue(20, start=3)
        self.assertEqual(qs.get_size(), 20)
        customer = Customer.objects.get(pk='1')
        order = create_order(customer, 'more pizza!', Queue.objects.get(store_name='One').id)
        qs.place_order(order)
        self.assertEqual(qs.get_size(), 21)
        self.assertEqual(order.cancelled, False)
        self.assertEqual(order.priority, 21)
        fill_queue(20, start=30)
        thirtieth = Order.objects.get(customer=30)
        self.assertEqual(thirtieth.priority, 22)
        order.refresh_from_db()
        qs.cancel_order(order)
        self.assertEqual(order.cancelled, True)
        self.assertEqual(qs.get_size(), 40)
        thirtieth.refresh_from_db()
        self.assertEqual(thirtieth.priority, 21)

    def test_cancel_already_cancelled(self):
        customer = Customer.objects.get(pk='1')
        order = create_order(customer, 'pizza', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order)
        self.assertEqual(order.cancelled, False)
        self.assertEqual(order.priority, 1)
        qs.cancel_order(order)
        self.assertEqual(order.cancelled, True)
        self.assertEqual(qs.get_size(), 0)
        order.refresh_from_db()
        self.assertRaises(OrderCancelError, qs.cancel_order, order)
        self.assertEqual(order.cancelled, True)
        self.assertEqual(order.priority, 0)

    def test_swap_on_two_adjacent_orders(self):
        fill_queue(2, start=3)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        four = Order.objects.get(customer=4)
        three = Order.objects.get(customer=3)
        qs.swap(four, three)
        three.refresh_from_db()
        four.refresh_from_db()
        self.assertEqual(three.priority, 2)
        self.assertEqual(four.priority, 1)

    def test_swap_on_two_adjacent_orders_already_in_right_order(self):
        fill_queue(2, start=3)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        four = Order.objects.get(customer=4)
        three = Order.objects.get(customer=3)
        self.assertRaises(SwapError, qs.swap, three, four)
        three.refresh_from_db()
        four.refresh_from_db()
        self.assertEqual(three.priority, 1)
        self.assertEqual(four.priority, 2)

    def test_swap_on_filled_or_cancelled(self):
        fill_queue(2, start=3)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        four = Order.objects.get(customer=4)
        three = Order.objects.get(customer=3)
        qs.cancel_order(three)
        self.assertRaises(SwapError, qs.swap, four, three)
        three.refresh_from_db()
        four.refresh_from_db()
        self.assertEqual(three.priority, 0)
        self.assertEqual(four.priority, 1)

    def test_fill_single_order(self):
        customer = Customer.objects.get(pk='1')
        order = create_order(customer, 'pizza', Queue.objects.get(store_name='One').id)
        qs = QueueService(Queue.objects.get(store_name='One').id)
        qs.place_order(order)
        qs.pop()
        order.refresh_from_db()
        self.assertEqual(order.priority, 0)
        self.assertEqual(qs.get_size(), 0)
        self.assertEqual(order.filled, True)










