__author__ = 'Sean'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^signin/$', views.sign_in_page, name='sign_in'),
    url(r'^$', views.home, name='home'),
    url(r'^/$', views.home, name='home'),
    #use the single details url post = change, get to display form
    url(r'^details/P?()$', views.details, name='details'),
    url(r'^create_account/$', views.create_account, name='create_account')

]