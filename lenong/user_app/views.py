from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from hashlib import *
from django import forms
from django.template import RequestContext
from LenongGongsApp import models
# from models import UserInfo


# Create your views here.
def register(request):
    return render(request, 'register.html')


def register_handle(request):
    # 接收用户输入 密码  确认密码  邮箱
    uname = request.POST.get('user_name', '无')
    upwd = request.POST.get('pwd', '无')
    upwd2 = request.POST.get('cpwd', '无')
    uemail = request.POST.get('email', '无')
    # 判断两次密码
    if upwd != upwd2:
        # 如果没有密码不一致 我们就直接重定向返回注册页
        return redirect('/user/register/')
        # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf8'))
    upwd3 = s1.hexdigest()
    # 创建模型类对象
    user = models.UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')


def login(request):
    return render(request, 'login.html')


def glogin(request):
    uname = request.POST('username')
    upwd = request.POST('pwd')
    b = models.UserInfo.objects.get(uname=uname)
    if b.upwd == upwd:
        a = models.TypeInfo.objects.all()
        fresh_fruits = models.GoodsInfo.objects.filter(gtype_id=6)  # 新鲜水果
        seafood_aquaculture = models.GoodsInfo.objects.filter(gtype_id=7)  # 海鲜水产
        poultry = models.GoodsInfo.objects.filter(gtype_id=8)  # 禽类蛋品
        vegetables = models.GoodsInfo.objects.filter(gtype_id=9)  # 蔬菜
        quick_frozen_food = models.GoodsInfo.objects.filter(gtype_id=10)  # 速冻食品
        fruDic = {'title': a.get(pk=6), 'text': fresh_fruits[0:4], 'id': 6}
        seafoodDic = {'title': a.get(pk=7), 'text': seafood_aquaculture[0:4], 'id': 7}
        poultryDic = {'title': a.get(pk=8), 'text': poultry[0:4], 'id': 8}
        vegetablesDic = {'title': a.get(pk=9), 'text': vegetables[0:4], 'id': 9}
        quickDic = {'title': a.get(pk=10), 'text': quick_frozen_food[0:4], 'id': 10}
        context = [fruDic, seafoodDic, poultryDic, vegetablesDic, quickDic]
        return render(request, 'index.html', {'context': context,'b':b})
    else:
        return render(request,'404.html')
