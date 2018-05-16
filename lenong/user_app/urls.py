from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register/$',views.register,name='register'),
    url(r'handle/$',views.register_handle,name='handle'),
    url(r'login/$',views.login,name='login'),
    url(r'glogin/',views.glogin,name='glogin')

]