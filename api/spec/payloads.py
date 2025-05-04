from pydantic import BaseModel

class AlunoPayload(BaseModel):
    nome: str
    idade: int
    data_nascimento: str
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    turma_id: int

class ProfessorPayload(BaseModel):
    nome: str
    idade: int
    materia: str
    observacoes: str

class TurmaPayload(BaseModel):
    descricao: str
    professor_id: int
    ativo: bool