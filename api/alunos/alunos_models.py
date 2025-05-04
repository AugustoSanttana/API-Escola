from database import DatabaseManager

class ModelAlunos():

  def __init__(self) -> None:
     ...

  def get_alunos(self) -> list:
    alunos_db = DatabaseManager().select_all('SELECT * FROM alunos')
    return [aluno._asdict() for aluno in alunos_db] if alunos_db else []
  
  def get_aluno_by_id(self, id: int) -> dict:
    aluno_db = DatabaseManager().select_one(f"SELECT * FROM alunos WHERE id = {id}")
    return aluno_db._asdict() if aluno_db else {}
  
  def post_aluno(self, novo_aluno: dict) -> dict:
    ids_turmas_cadastradas = [id[0] for id in DatabaseManager().select_all("SELECT id FROM turmas")]

    if novo_aluno["turma_id"] not in ids_turmas_cadastradas:
        return {"error": "turma não existe", "status_code": 404}

    DatabaseManager().execute_sql_str(f"INSERT INTO alunos(nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final) VALUES('{novo_aluno.get('nome')}', {novo_aluno.get('idade')}, {novo_aluno.get('turma_id')}, '{novo_aluno.get('data_nascimento')}', {novo_aluno.get('nota_primeiro_semestre')}, {novo_aluno.get('nota_segundo_semestre')}, {novo_aluno.get('media_final')})")
    return {"msg":"aluno cadastrado com sucesso"}
  
  def delete_aluno(self, id: int) -> bool:
    aluno_db_deletar = DatabaseManager().select_one(F"SELECT * FROM alunos WHERE id = {id}")
    if not aluno_db_deletar:
      return False
    DatabaseManager().execute_sql_str(f"DELETE FROM alunos WHERE id = {id}")
    return True
  
  def update_aluno(self, id: int, aluno_atualizado: dict) -> dict:

    aluno_db_atualizar = DatabaseManager().select_one(F"SELECT * FROM alunos WHERE id = {id}")

    if not aluno_db_atualizar:
      return {"error":"aluno não encontrado para atualização"}

    ids_turmas_cadastradas = [id[0] for id in DatabaseManager().select_all("SELECT id FROM turmas")]

    if aluno_atualizado["turma_id"] not in ids_turmas_cadastradas:
      return {"error":"turma não existe"}

    DatabaseManager().execute_sql_str(f"""
      UPDATE alunos
      SET nome = '{aluno_atualizado.get('nome')}',
        idade = {aluno_atualizado.get('idade')},
        turma_id = {aluno_atualizado.get('turma_id')},
        data_nascimento = '{aluno_atualizado.get('data_nascimento')}',
        nota_primeiro_semestre = {aluno_atualizado.get('nota_primeiro_semestre')},
        nota_segundo_semestre = {aluno_atualizado.get('nota_segundo_semestre')},
        media_final = {aluno_atualizado.get('media_final')}
      WHERE id = {id}
    """)
    return {"msg":"aluno atualizado com sucesso"}


    








