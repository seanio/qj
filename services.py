__author__ = 'Sean'
from .models import Queue, Customer, Order
from django.db.models import Max



class QueueService:

    def __init__(self, store):
        self.queue = Queue.objects.get(pk=store)


    #swaps two people in the queue
    def swap(self, order_up, order_down):
        if order_down.priority >= order_up.priority:
            raise SwapError("Order 1 is already above order 2")
        if order_down.priority <= 0 or order_up.priority <= 0:
            raise SwapError("One of the orders isn't active")
        tmp = order_up.priority
        order_up.priority = order_down.priority
        order_up.save()
        order_down.priority = tmp
        order_down.save()
        return self

    #pop the first off the queue and update priorities
    def pop(self):
        order = Order.objects.all().filter(queue=self.queue.id).get(priority=1)
        below_orders = Order.objects.all().filter(queue=self.queue.id).filter(priority__gt=order.priority)
        self.move_up_queue(below_orders)
        order.priority = 0
        order.filled = True
        order.save()
        return self

    #jump someone as high as they can go
    def jump(self, order):
        return self

    #place an order with the right priority
    def place_order(self, order):
        last_order = Order.objects.all().filter(queue=self.queue.id).aggregate(Max('priority'))
        if last_order['priority__max'] == -1:
            order.priority = 1
        else:
            order.priority = last_order['priority__max'] + 1
        order.save()
        return

    def cancel_order(self, order):
        if order.cancelled:
            raise OrderCancelError("Order already cancelled")
        below_orders = Order.objects.all().filter(queue=self.queue.id).filter(priority__gt=order.priority)
        self.move_up_queue(below_orders)
        order.priority = 0
        order.cancelled = True
        order.save()
        return self

    @staticmethod
    def move_up_queue(orders):
        for order in orders:
            order.priority -= 1
            order.save()
        return

    def get_size(self):
        active_orders = Order.objects.all().filter(queue=self.queue.id).filter(cancelled=False).filter(filled=False)
        return active_orders.count()

class OrderCancelError(Exception):
    def __init__(self, value):
         self.value = value

class SwapError(Exception):
    def __init__(self, value):
         self.value = value


