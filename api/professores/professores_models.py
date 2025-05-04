from database import DatabaseManager

class ModelProfessores():

  def __init__(self) -> None:
    ...
    
  def get_professores(self) -> list:
    professores_db = DatabaseManager().select_all("SELECT * FROM professores")
    return [professor._asdict() for professor in professores_db] if professores_db else []
  
  def get_professores_by_id(self, id: int) -> dict:
    professor_db = DatabaseManager().select_one(f"SELECT * FROM professores WHERE id = {id}")
    return professor_db._asdict() if professor_db else {}
  
  def post_professor(self, novo_professor: dict) -> dict:
    DatabaseManager().execute_sql_str(f"INSERT INTO professores(nome, idade, materia, observacoes) VALUES('{novo_professor.get('nome')}', {novo_professor.get('idade')}, '{novo_professor.get('materia')}', '{novo_professor.get('observacoes')}')")
    return {"msg":"professor cadastrado com sucesso"}
  
  def delete_professor(self, id: int) -> bool:

    professor_db_deletar = DatabaseManager().select_one(f"SELECT * FROM professores WHERE id = {id}")
    if not professor_db_deletar:
      return False
    DatabaseManager().execute_sql_str(f"DELETE FROM professores WHERE id = {id}")
    return True
  
  def update_professor(self, id: int, professor_atualizado: dict) -> dict:

    professor_db_atualizar = DatabaseManager().select_one(f"SELECT * FROM professores WHERE id = {id}")

    if not professor_db_atualizar:
      return {"error":"professor não encontrado para atualização"}
        

    
    DatabaseManager().execute_sql_str(f"""UPDATE professores
      SET nome = '{professor_atualizado['nome']}',
      idade = {professor_atualizado['idade']},
      materia = '{professor_atualizado['materia']}',
      observacoes = '{professor_atualizado['observacoes']}'
      WHERE id = {id}"""
    )
    return {"msg":"professor atualizado com sucesso"}
    
