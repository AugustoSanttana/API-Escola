from database import banco_de_dados

alunos: list = banco_de_dados['alunos']
turmas: list = banco_de_dados['turmas']


class ModelAlunos():

  def __init__(self) -> None:
     ...

  def get_alunos(self) -> list:
    if alunos:
      return alunos
    return []
  
  def get_aluno_by_id(self, id: int) -> dict:
    for aluno in alunos:
      if aluno["id"] == id:
        return aluno
    return {}
  
  def post_aluno(self, novo_aluno: dict) -> dict:
    ids_cadastrados = [aluno["id"] for aluno in alunos]
    ids_turmas_cadastradas = [turma["id"] for turma in turmas]

    if novo_aluno["id"] in ids_cadastrados:
        return {"error": "id do aluno ja utilizado", "status_code": 400}

    if novo_aluno["turma_id"] not in ids_turmas_cadastradas:
        return {"error": "turma não existe", "status_code": 404}

    alunos.append(novo_aluno)
    return {"msg":"aluno cadastrado com sucesso"}
  
  def delete_aluno(self, id: int) -> bool:
    for aluno in alunos:
      if aluno["id"] == id:
        alunos.remove(aluno)
        return True
    return False
  
  def update_aluno(self, id: int, aluno_atualizado: dict) -> dict:
    ids_turmas_cadastradas = [turma["id"] for turma in turmas]

    if aluno_atualizado["turma_id"] not in ids_turmas_cadastradas:
      return {"error":"turma não existe"}

    for index, aluno in enumerate(alunos):
      if aluno.get("id") == id:
        aluno_atualizado["id"] = id
        alunos[index] = aluno_atualizado
        return {"msg":"aluno atualizado com sucesso"}

    return {"error":"aluno não encontrado para atualização"}

    








