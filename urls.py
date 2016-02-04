__author__ = 'Sean'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signin/$', views.sign_in_page, name='sign_in'),
    url(r'^$', views.home, name='home'),
    url(r'^/$', views.home, name='home')

]