from django.db import models
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingFormField
from django.conf import settings
from django.conf.urls.static import static
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)  # 标题
    gpic = models.ImageField(upload_to='static/media/')  # 图片
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 价格
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gtype = models.ForeignKey(TypeInfo)  # 商品分类的外键关系
    gclick = models.IntegerField(default=0)  # 点击量  用于排序
    gunit = models.CharField(max_length=20, default='500g')  # 单位
    gjianjie = models.CharField(max_length=200)  # 简介
    gcontent = models.TextField()#全部内容
    gpub_date = models.DateTimeField(datetime.datetime.now())  # 上架时间
    gpubj_date = models.DateTimeField()  # 下架时间

    def __str__(self):
        return self.gtitle
