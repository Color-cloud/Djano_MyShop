from django.db.models import Sum
from django.shortcuts import render

from APPS.home.models import *


def shop_detail(request):
    if request.method == 'GET':
        uid=request.user.id
        count = ShopCar.objects.filter(user_id=uid,status=1).aggregate(
            sum=Sum('number')).get('sum')
        id = request.GET.get('id')
        shop = Shop.objects.get(shop_id=id)
        img = shop.shopimage_set.all().first()
        secs = shop.propertyvalue_set.all()
        return render(request, 'shopdetail.html', {'shop': shop, 'img': img, 'secs': secs,'uid':uid,'count':count})
