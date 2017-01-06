from appssgr.models import *


professores=Grupo(name="Professores")
professores.save()
alunos=Grupo(name="Alunos")
alunos.save()

# Criando as pessoas
pes1=Pessoa(is_staff=True,first_name='Givanaldo', last_name="Rocha", cpf='33344455560',email='givanaldo@gmail.com',
            data_nascimento="1973-05-30", telefone='8499253259' ,username='20122148000001')
pes1.set_password('123456')
pes1.save()
pes2=Pessoa(is_staff=True,first_name='Carlos Henrique', last_name='Pires dos Santos', cpf='33344455561',email='carlos@gmail.com',
            data_nascimento="1999-05-30", telefone='84998217953' ,username='20122148000002')
pes2.set_password('123456')
pes2.save()
alunos.user_set.add(pes2)

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
alu1 = Aluno(pessoa=pes2,cursos=tsi)
alu1.save()

# Tipo Requerimento
tipo1 = TipoRequerimento(nome="Reposição de Atividades")
tipo1.save()

# Documento
doc1 = Documento(nome="Atestado Médico")
doc1.save()

# Criando Requerimento
req1 = Requerimento(aluno=alu1,data_solicitacao_requerimento="2017-01-25",tipo_requerimento=tipo1,disciplina=web1,observacoes="Teste",
                    justificava="Consulta Médica",data_atividade="2017-01-10",tipo_atividade="Prova",professor_atividade=prof1)
req1.save()
req1.documentos_apresentados.add(doc1)
