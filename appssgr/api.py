from tastypie.resources import ModelResource
from tastypie import fields
from .models import Professor,Pessoa

class PessoaResource(ModelResource):

    class Meta:
        queryset = Pessoa.objects.all()
        resource_name='pessoa'
        fields=['username','first_name','last_name']

class ProfessorResource(ModelResource):
    pessoa=fields.ToOneField('appssgr.api.PessoaResource','pessoa',full=True)
    class Meta:
        queryset = Professor.objects.all()
        resource_name='professor'
