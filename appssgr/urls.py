from django.conf.urls import include,url
from appssgr.views import *
from django.contrib.auth.views import login,logout

urlpatterns=[
# Url para a página principal base.html
    url(r'^$',home,name='home'),

# Urls para Login e Logout
    url(r'^login/$',login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^curso/$',curso,name='curso'),
    url(r'^erro_permissao/$', erro_permissao, name='erro_permissao'),

# Urls para os requerimentos
    url(r'^req/list/$',req_list,name='req_list'),
    url(r'^req/list/deferidos$',req_list_deferidos,name='req_list_deferidos'),
    url(r'^req/list/indeferidos$', req_list_indeferidos, name='req_list_indeferidos'),
    url(r'^req/new/$',req_new,name='req_new'),
    url(r'^req/update/(?P<pk>\d+)$',req_update,name='req_update'),
    url(r'^req/detail/(?P<pk>\d+)$', req_detail, name='req_detail'),
    #url(r'^req/delete/(P<pk>\d+)$',req_delete,name='req_delete'),
]
