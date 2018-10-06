from django.shortcuts import render

from APPS.home.models import Shop, ShopImage


def search(request):
    # 获取到前端输入的要搜索商品名称
    want_to = request.GET.get('want_to')
    shops = Shop.objects.filter(name__icontains=want_to).values('shop_id', 'name', 'promote_price')
    for shop in shops:
        img = ShopImage.objects.filter(shop_id=shop['shop_id']).first().shop_img_id
        shop.update(img=img)
    return render(request, 'search_result.html', {'shops': shops})
