from database import DatabaseManager

class ModelAdmin():
    def __init__(self) -> None:
        ...
    
    def resetar(self):
        db = DatabaseManager()
        db.execute_sql_str("DROP TABLE IF EXISTS alunos CASCADE;")
        db.execute_sql_str("DROP TABLE IF EXISTS turmas CASCADE;")
        db.execute_sql_str("DROP TABLE IF EXISTS professores CASCADE;")

        db.execute_sql_str("""
            CREATE TABLE professores (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                idade INTEGER NOT NULL,
                materia VARCHAR(100) NOT NULL,
                observacoes TEXT
            );
        """)
        
        db.execute_sql_str("""
            CREATE TABLE turmas (
                id SERIAL PRIMARY KEY,
                descricao VARCHAR(100) NOT NULL,
                professor_id INTEGER,
                ativo BOOLEAN NOT NULL,
                FOREIGN KEY (professor_id) REFERENCES professores(id)
            );
        """)

        db.execute_sql_str("""
            CREATE TABLE alunos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                idade INTEGER NOT NULL,
                turma_id INTEGER,
                data_nascimento DATE NOT NULL,
                nota_primeiro_semestre FLOAT,
                nota_segundo_semestre FLOAT,
                media_final FLOAT,
                FOREIGN KEY (turma_id) REFERENCES turmas(id) ON DELETE SET NULL
            );
        """)