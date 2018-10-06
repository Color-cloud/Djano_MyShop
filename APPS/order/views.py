import datetime
import random

from django.contrib.auth.models import User
from django.shortcuts import render

from APPS.home.models import *


def myorder(request):
    order_code = f'{datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")}{random.randint(10, 99)}'
    shopid = request.GET.get('sid')
    shopnumber = request.GET.get('number')
    uname= request.GET.get('uname')
    user= User.objects.filter(username=uname).first()
    shop = Shop.objects.filter(shop_id=shopid).first()
    single_price = shop.promote_price
    money=int(shopnumber)*single_price
    order = Order(order_code=order_code, address='泰国新加坡', mobile=124324213, receiver='Father', user_message='测试测试测试测试测试测试',
                  user=request.user.userprofile)
    order.save()
    return render(request,'order_detail.html',{'shop':shop,'user':user,'money':money})
