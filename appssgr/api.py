from tastypie.resources import ModelResource
from tastypie import fields
from .models import Professor,Pessoa
'''
Esse arquivo contém a API rest usando o tastypie que é um framework em cima do Django para construção de WebServices do tipo REST
Página com a documentação: https://django-tastypie.readthedocs.io/en/latest/

Como estamos interessados em criar WebServices para fornecer dados, criamos o que o TasyPie chama de Resource(recurso) para servir
como requisição WEB

No Caso criei dois recursos, relacionado a Pessoa(User) e Professor

'''

class PessoaResource(ModelResource):

    class Meta:
        queryset = Pessoa.objects.all() #Define qual a fonte de dados, ou seja, que consulta vai ser feita
        resource_name='pessoa' #Nome do recurso a ser usado na url de requisição
        fields=['username','first_name','last_name'] #Campos que serão disponibilizados, relaciondas a Pessoa

class ProfessorResource(ModelResource):
    # Como Professor tem relacionamento com pessoa, é necessário criar um relacionamento entre Resources, indicando a classe que vai servir
    # os dados necessários (PessoaResource) e se deve recuperar os dados ou apenas trazer uma referências
    pessoa=fields.ToOneField('appssgr.api.PessoaResource','pessoa',full=True)
    class Meta:
        queryset = Professor.objects.all()
        resource_name='professor'
