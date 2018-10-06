from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from APPS.home.models import ShopCar


def shouye(request):
    return render(request, 'shouye.html')
