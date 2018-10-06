from django.shortcuts import render, redirect
from alipay import AliPay

from Djano_MyShop import settings


def pay(request):
    money= request.GET.get('money')
    #创建支付宝对象
    alipay=AliPay(appid=settings.APP_ID,
           app_notify_url=None,
           app_private_key_string=settings.APP_PRIVATE_STRING,
           alipay_public_key_string=settings.APP_PUBLIC_STRING,
           debug=True
           )
    #生成订单数据
    order_url=alipay.api_alipay_trade_page_pay(
        subject='测试支付TheOne',
        out_trade_no='666',
        total_amount=money,
        #支付成功后跳转到前端  get
        return_url='https://www.baidu.com',
        #后台接受支付宝支付相关的信息的接口  post
        # notify_url=
    )
    pay_url = settings.ALI_PAY_DEV_URL + order_url
    return redirect(pay_url)
#支付成功跳转的url
def notify_callback(request):
    pass