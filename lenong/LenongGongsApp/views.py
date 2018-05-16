from django.shortcuts import render
from LenongGongsApp import models
from user_app import models


# Create your views here.
def index(request):
    a = models.TypeInfo.objects.all()
    fresh_fruits = models.GoodsInfo.objects.filter(gtype_id=6)  # 新鲜水果
    seafood_aquaculture = models.GoodsInfo.objects.filter(gtype_id=7)  # 海鲜水产
    poultry = models.GoodsInfo.objects.filter(gtype_id=8)  # 禽类蛋品
    vegetables = models.GoodsInfo.objects.filter(gtype_id=9)  # 蔬菜
    quick_frozen_food = models.GoodsInfo.objects.filter(gtype_id=10)  # 速冻食品
    fruDic = {'title': a.get(pk=6), 'text': fresh_fruits[0:4],'id':6}
    seafoodDic = {'title': a.get(pk=7), 'text': seafood_aquaculture[0:4],'id':7}
    poultryDic = {'title': a.get(pk=8), 'text': poultry[0:4],'id':8}
    vegetablesDic = {'title': a.get(pk=9), 'text': vegetables[0:4],'id':9}
    quickDic = {'title': a.get(pk=10), 'text': quick_frozen_food[0:4],'id':10}
    context = [fruDic, seafoodDic, poultryDic, vegetablesDic, quickDic]
    return render(request, 'index.html', {'context': context})


def tupian(request, type_id):
    a = models.GoodsInfo.objects.filter(gtype_id=type_id)
    return render(request, 'list.html', {'a': a})
def detail(request,type_id):
    a = models.GoodsInfo.objects.filter(pk=type_id)
    return render(request, 'detail.html',{'a':a})
