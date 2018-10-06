from django.db.models import Sum
from django.shortcuts import render

from APPS.home.models import *


# 左侧分类表及其扩展
def LeftTable(request):
    count = ShopCar.objects.filter(user_id=request.user.id).aggregate(sum=Sum('number')).get('sum')
    # 轮播图
    banns = Banner.objects.all()
    # 横向导航栏
    nav = Navigation.objects.all()
    # 第一级分类
    Firsts = Category.objects.all()
    for First in Firsts:
        # 第二级分类
        First.Seconds = First.submenu_set.all()
        for Second in First.Seconds:
            # 第三级分类
            Second.Thirts = Second.submenu2_set.all()
    # 界面下方显示的商品信息
    shops = Shop.objects.all()
    for shop in shops:
        shop.img = shop.shopimage_set.filter(shop_id=shop.shop_id).first().shop_img_id
    return render(request, 'shouye.html',
                  {'nav': nav, 'Firsts': Firsts, 'banns': banns, 'shops': shops, 'count': count})
