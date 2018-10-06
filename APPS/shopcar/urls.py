from django.conf.urls import url, include
from django.contrib import admin
#
from APPS.shopcar import views

urlpatterns = [
    url('shopadd/', views.add, name='shopadd'),
]