from django.forms import ModelForm, forms
from appssgr.models import *

class RequerimentoForm(ModelForm):
    class Meta:
        model=Requerimento
        fields=('__all__')

#Form tratando o readOnly para não editar outros campos do formulário, além de encaminhar e e situação
class RequerimentoFormUpdate(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequerimentoFormUpdate, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['readonly'] = True
            self.fields[f].widget.attrs['disabled'] = True
        self.fields['situacao'].widget.attrs['readonly'] = False
        self.fields['encaminhado_para'].widget.attrs['readonly'] = False
        self.fields['observacoes'].widget.attrs['readonly'] = False
        self.fields['situacao'].widget.attrs['disabled'] = False
        self.fields['encaminhado_para'].widget.attrs['disabled'] = False
        self.fields['observacoes'].widget.attrs['disabled'] = False
    class Meta:
        model=Requerimento

        fields=('__all__')


