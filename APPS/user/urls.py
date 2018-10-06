from django.conf.urls import url

from APPS.user import views

urlpatterns = [
    url('denglu/', views.mylogin, name='denglu'),
    url('zhuce/',views.zhuce,name='zhuce'),
    url('dengchu/', views.dengchu, name='dengchu')

]
