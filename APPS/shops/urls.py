from django.conf.urls import url, include
from django.contrib import admin
#
from APPS.shops import views

urlpatterns = [
    url('shopdetail/', views.shop_detail, name='shopdetail'),
]