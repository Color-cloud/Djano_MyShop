import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import  User
from django.shortcuts import render, redirect

from APPS.home.models import *


def mylogin(request):
    if request.method == 'GET':
        return render(request, 'denglu.html')
    elif request.method == 'POST':
        username = request.POST.get('srusername')
        password = request.POST.get('srpassword')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/',{'user':user})
        else:
            return render(request,'denglu.html',{'msg':'用户名或密码输入错误'})
def zhuce(request):
    if request.method=='GET':
        return render(request,'zhuce.html')
    elif request.method == 'POST':
        username=request.POST.get('zcusername')
        password=request.POST.get('zcpassword')
        qr=request.POST.get('qrpassword')
        if qr==password:
            user=User.objects.create_user(username=username,password=password)
            UserProfile.objects.create(user_id=user.id)
        else:
            return render(request,'zhuce.html',{'msg':'两次输入密码不一致'})
        return redirect('/')
def dengchu(request):
    logout(request)
    return redirect('/')