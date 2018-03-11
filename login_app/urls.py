# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'signup/$', views.signup, name='signup'),
]