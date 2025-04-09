from database import banco_de_dados

professores: list = banco_de_dados["professores"]

class ModelProfessores():

  def __init__(self) -> None:
    ...
    
  def get_professores(self) -> list:
    if professores:
      return professores
    return []
  
  def get_professores_by_id(self, id: int) -> dict:
    for professor in professores:
      if professor["id"] == id:
        return professor
    return {}
  
  def post_professor(self, novo_professor: dict) -> dict:
    ids_cadastrados = [professor["id"] for professor in professores]
    
    if novo_professor["id"] in ids_cadastrados:
        return {"error": "id do aluno ja utilizado", "status_code": 400}
      
    professores.append(novo_professor)
    return {"msg":"professor cadastrado com sucesso"}
  
  def delete_professor(self, id: int) -> bool:
    for professor in professores:
      if professor["id"] == id:
        professores.remove(professor)
        return True
    return False
  
  def update_professor(self, id: int, professor_atualizado: dict) -> dict:
    
    for index, professor in enumerate(professores):
      if professor.get("id") == id:
        professor_atualizado["id"] = id
        professores[index] = professor_atualizado
        return {"msg":"professor atualizado com sucesso"}
      
    return {"error":"professor não encontrado para atualização"}
        
