from _pydecimal import _group_lengths

from appssgr.models import *

professores=Group(name="Professores")
professores.save()
alunos=Group(name="Alunos")
alunos.save()
tecadm=Group(name="Técnico Administrativo")
tecadm.save()

# Criando as pessoas
pes1=Pessoa(is_staff=True,first_name='Givanaldo', last_name="Rocha", cpf='33344455560',email='givanaldo@gmail.com',
            data_nascimento="1973-05-30", telefone='8499253259' ,username='20122148000001')
pes1.set_password('123456')
pes1.save()
professores.user_set.add(pes1)

pes4=Pessoa(first_name='Eduardo', last_name="Chavez", cpf='55566633301',email='eduardo@gmail.com',data_nascimento="1989-05-15",username='20122148000004',  telefone='84955196660')
pes4.set_password('123456')
pes4.save()
tecadm.user_set.add(pes4)

# Criando os Professores
prof1 = Professor(pessoa=pes1)
prof1.save()

# Criando as Disciplinas
web1 = Disciplina(codigo="prowb1", nome="Programação Web I", carga_horaria=60, periodo=2)
web1.save()

# Criando o Curso
tsi = Curso(codigo="tsi14", nome="Tecnólogo Sistemas para Internet")
tsi.save()

# Criando os Alunos
alu1=Aluno(is_staff=True,first_name='Carlos Henrique', last_name='Pires dos Santos', cpf='33344455561',email='carlos@gmail.com',
            data_nascimento="1999-05-30", telefone='84998217953' ,username='20122148000002',cursos=tsi)
alu1.set_password('123456')
alu1.save()
alunos.user_set.add(alu1)

alu2=Aluno(is_staff=True,first_name='Juliana', last_name='dos Anjos', cpf='33344455562',email='juh@gmail.com',
            data_nascimento="1999-05-15", telefone='84998217913' ,username='20122148000003', cursos=tsi)
alu2.set_password('123456')
alu2.save()
alunos.user_set.add(alu2)

# Criando os Tecnico Administrativo
tecadm1=Tecnico_Administrativo(pessoa=pes4)
tecadm1.save()


# Tipo Requerimento
tipo1 = TipoRequerimento(nome="Reposição de Atividades")
tipo1.save()

# Documento
doc1 = Documento(nome="Atestado Médico")
doc1.save()

# Situação
sit1 = Situacao(tipo="Em Avaliação")
sit1.save()
sit2 = Situacao(tipo="Requerimento Deferido")
sit2.save()
sit3 = Situacao(tipo="Requerimento Indeferido")
sit3.save()




# Criando Requerimento
#req1 = Requerimento(aluno=alu1,tipo_requerimento=tipo1,disciplina=web1,observacoes="Teste",
#                    justificava="Consulta Médica",data_atividade="2017-01-10",tipo_atividade="Prova",professor_atividade=prof1)
#req1.save()
#req1.documentos_apresentados.add(doc1)

#req2 = Requerimento(aluno=alu2,tipo_requerimento=tipo1,disciplina=web1,observacoes="Teste",
#                    justificava="Consulta Médica",data_atividade="2017-01-02",tipo_atividade="Prova",professor_atividade=prof1)
#req2.save()
#req2.documentos_apresentados.add(doc1)