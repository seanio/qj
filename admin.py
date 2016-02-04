from django.contrib import admin
from .models import Customer, Queue, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Queue)