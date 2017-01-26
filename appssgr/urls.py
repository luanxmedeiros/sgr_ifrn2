from django.conf.urls import include,url
from appssgr.views import *
from tastypie.api import Api
from django.contrib.auth.views import login,logout
from .api import ProfessorResource,PessoaResource

'''
Aqui faremos a ligação da API REst com as urls do Django, para que seja possível fazer as requisições.
No caso criamos uma api chamada dados e aglutinamos os resources. Uma vez registrada a url, é possível realizar vários tipos de requisições
Exemplos de requisições
http://127.0.0.1:8000/appssgr/api/dados/professor/?format=json (Retorna todos os professores cadastrados:
Json de retorno:
{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1},
"objects": [{"pessoa": {"first_name": "Aldenor", "last_name": "Bezerra",
"resource_uri": "/appssgr/api/dados/pessoa/3/", "username": "289041"},
"resource_uri": "/appssgr/api/dados/professor/3/"}]}

Para a lista completa de urls que podem ser montadas, consultar a documentação do Tastypie

'''
api=Api(api_name='dados')
professorResource=ProfessorResource()
api.register(professorResource)
api.register(PessoaResource())

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
    url(r'^req/new/$',req_new,name='req_new'),
    url(r'^req/update/(?P<pk>\d+)$',req_update,name='req_update'),
    url(r'^req/detail/(?P<pk>\d+)$', req_detail, name='req_detail'),
    #url(r'^req/delete/(P<pk>\d+)$',req_delete,name='req_delete'),


#Urls para a API. api.urls gerar todos os endereços possíveis
    url(r'^api/',include(api.urls),name='api'),
]
