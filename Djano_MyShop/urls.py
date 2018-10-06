from django.conf.urls import url, include
from django.contrib import admin
#
from APPS.categoey import views
#
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',views.LeftTable),
    url('user/',include('APPS.user.urls')),
    url('category/',include('APPS.categoey.urls')),
    url('shops/', include('APPS.shops.urls')),
    url('shopcar/', include('APPS.shopcar.urls')),
    url('search/', include('APPS.search.urls')),
    url('order/',include('APPS.order.urls')),
    url('pay/', include('APPS.mypay.urls')),
]
