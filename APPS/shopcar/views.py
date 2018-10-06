from django.db.models import Sum, F
from django.http import JsonResponse
from django.shortcuts import render

from APPS.home.models import *


def shopcar_count(request):
    count = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1).aggregate(
        sum=Sum('number')).get('sum')
    return {'count': count}


def add(request):
    uid = request.user.userprofile.uid
    shop_id = request.POST.get('shop_id')
    number = request.POST.get('number')
    cars = ShopCar.objects.filter(user_id=uid, shop_id=shop_id, status=1)
    if cars:
        car = cars.first()
        car.number = F('number') + number
        car.save(update_fields=['number'])
    else:
        car = ShopCar(user_id=uid, shop_id=shop_id, number=number)
        car.save()
    data = shopcar_count(request)
    data['status'] = 200
    data['msg'] = 'success'
    return JsonResponse(data=data)
