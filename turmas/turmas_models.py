from database import banco_de_dados

turmas: list = banco_de_dados["turmas"]
professores: list = banco_de_dados["professores"]

class ModelTurmas():

  def __init__(self) -> None:
    ...
  def get_turmas(self) -> list:
    if turmas:
        return turmas
    return []
  
  def get_turmas_by_id(self, id: int) -> dict:
    for turma in turmas:
        if turma["id"] == id:
           return turma
    return {}
  
  
  def post_turma(self, nova_turma: dict) -> dict:
    ids_turmas = [turma["id"] for turma in turmas]
    ids_professores = [professor["id"] for professor in professores]

    if nova_turma["id"] in ids_turmas:
        return {"error": "id da turma já existente", "status_code": 409}

    if nova_turma["professor_id"] not in ids_professores:
        return  {"error": "professor não existe", "status_code": 404}

    turmas.append(nova_turma)
    return {"msg": "turma cadastrada com sucesso"}
  
  def delete_turma(self, id: int) -> bool:
    for turma in turmas:
        if turma["id"] == id:
            turmas.remove(turma)
            return True
    return False
  
  def update_turma(self, id: int, turma_atualizada: dict) -> dict:
    for index, turma in enumerate(turmas):
        if turma.get("id") == id:
            turma_atualizada["id"] = id
            turmas[index] = turma_atualizada
            return {"msg":"turma atualizada com sucesso"}
        
    return {"error":"turma não encontrada para atualização"}

    
       
