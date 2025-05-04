from database import DatabaseManager

class ModelTurmas():

  def __init__(self) -> None:
    ...
  def get_turmas(self) -> list:
    turmas_db = DatabaseManager().select_all("SELECT * FROM turmas")
    return [turma._asdict() for turma in turmas_db] if turmas_db else []
  
  def get_turmas_by_id(self, id: int) -> dict:
    turma_db = DatabaseManager().select_one(f"SELECT * FROM turmas WHERE id = {id}")
    return turma_db._asdict() if turma_db else {}
  
  def post_turma(self, nova_turma: dict) -> dict:
    ids_professores = [id[0] for id in DatabaseManager().select_all("SELECT id FROM professores")]

    if nova_turma["professor_id"] not in ids_professores:
      return  {"error": "professor não existe", "status_code": 404}

    DatabaseManager().execute_sql_str(f"INSERT INTO turmas(descricao, professor_id, ativo) VALUES('{nova_turma.get('descricao')}', {nova_turma.get('professor_id')}, {nova_turma.get('ativo')})")
    return {"msg": "turma cadastrada com sucesso"}
  
  def delete_turma(self, id: int) -> bool:
    turma_db_deletar = DatabaseManager().select_one(f"SELECT * FROM turmas WHERE id = {id}")
    if not turma_db_deletar:
      return False
    DatabaseManager().execute_sql_str(f"DELETE FROM turmas WHERE id = {id}")
    return True

  def update_turma(self, id: int, turma_atualizada: dict) -> dict:

    ids_professores = [id[0] for id in DatabaseManager().select_all("SELECT id FROM professores")]
    if turma_atualizada.get("professor_id") not in ids_professores:
      return {"error":"id professor não existe"}

    turma_db_atualizar = DatabaseManager().select_one(f"SELECT * FROM turmas WHERE id = {id}")
    if not turma_db_atualizar:
      return {"error":"turma não encontrada para atualização"}
    
    DatabaseManager().execute_sql_str(f"UPDATE turmas SET descricao = '{turma_atualizada.get('descricao')}', professor_id = {turma_atualizada.get('professor_id')}, ativo = {turma_atualizada.get('ativo')} WHERE id = {id}")
    return {"msg":"turma atualizada com sucesso"}

    
       
