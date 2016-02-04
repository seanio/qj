from django.shortcuts import render, get_object_or_404
from .models import Customer, Order, Queue
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout



# Order detail page for a made order. Will list when it is expected and options for jumping the queue
# for a new order will display text saying you've placed your order
@login_required(login_url='/queuejumper/login')
def order_detail(request, order, new=False):
    details = get_object_or_404(Order, pk=order)
    return render(request, 'queuejumper/orderDetail.html', {'order': order, "new": new})


@login_required(login_url='/queuejumper/login')
def place_order(request, order):
    # logic to place an order
    return order_detail(request, order)


# home page once logged on. Can place an order with and choose options to jump
@login_required(login_url='/queuejumper/login')
def home(request):
    customer = Customer.objects.get(username=request.user.username)
    return render(request, 'queuejumper/home.html')


def login(request):
    template_response = views.login(request)
    return template_response


def create_account(request):
    User.objects.create_user(request.POST.username, request.POST.email, request.POST.password)
    user = authenticate(username=request.POST.username, password=request.POST.password)
    return render(request, 'queuejumper/home.html', {'customer': Customer.objects.get(username=user.username)})


def sign_in_page(request):
    form = AuthenticationForm()
    return render(request, 'queuejumper/templates/registration/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    '''some change'''
    return home(request)

'''I need to look up the template names for the registration thingos and put in the boilerplate'''
