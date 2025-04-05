from database import banco_de_dados
from pydantic import ValidationError



class AlunoNaoEncontrado(Exception):
    pass

  
def aluno_por_id(id_aluno):
  lista_alunos = banco_de_dados["alunos"]
  for dicionario in lista_alunos:
    if dicionario["id"] == id_aluno:
      return dicionario
  raise AlunoNaoEncontrado

def listar_alunos():
  return banco_de_dados["alunos"]

def adicionar_aluno(novo_aluno):
    banco_de_dados["alunos"].append(novo_aluno)     










