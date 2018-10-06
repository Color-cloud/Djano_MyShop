from django.conf.urls import url, include
from django.contrib import admin
#

#
from APPS.mypay import views

urlpatterns = [
    url('alipay/',views.pay),
]
