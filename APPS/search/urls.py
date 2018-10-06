from django.conf.urls import url, include
from django.contrib import admin
from APPS.search import views
urlpatterns = [

    url('search/', views.search),

]
