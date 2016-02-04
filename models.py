from django.db import models
from django.utils import timezone

# Create your models here.


class Queue(models.Model):
    store_name = models.CharField(max_length=200)
    def __str__(self):
        return self.store_name

class Customer(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    maxjumps = models.IntegerField(default=0)
    balance = models.FloatField(default=0)
    credit = models.FloatField(default=0)
    def __str__(self):
        return self.username

class Order(models.Model):
    priority = models.IntegerField(default=-1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    time_placed = models.DateTimeField(default=timezone.now())
    filled = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    been_jumped = models.IntegerField(default=0)
    has_jumped = models.IntegerField(default=0)
    details = models.CharField(max_length=300)
    def __str__(self):
        return " ".join([self.customer.username, self.details, str(self.id)])


