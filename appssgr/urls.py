from django.conf.urls import include,url
from appssgr.views import *
from django.contrib.auth.views import login,logout

urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^login/$',login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^curso/$',curso,name='curso')
]