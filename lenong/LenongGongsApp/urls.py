from django.conf.urls import include, url
from LenongGongsApp import views

urlpatterns = [
    url(r'^index/',views.index, name='index'),
    url(r'^tupian/(?P<type_id>[0-9]+)/$',views.tupian, name='tupian'),
    url(r'^detail/(?P<type_id>[0-9]+)/$',views.detail, name='detail')
]