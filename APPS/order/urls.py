from django.conf.urls import url, include
from django.contrib import admin
#
from APPS.order import views
#
urlpatterns = [
    url('order/',views.myorder),
]
