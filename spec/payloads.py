from pydantic import BaseModel

class CreateAlunoPayload(BaseModel):
    id: int
    nome: str
    idade: int
    data_nascimento: str
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    media_final: float
    turma_id: int

class UpdateAlunoPayload(BaseModel):
    nome: str
    idade: int
    data_nascimento: str
    nota_primeiro_semestre: float
    nota_segundo_semestre: float
    media_final: float
    turma_id: int

class CreateProfessorPayload(BaseModel):
    id: int
    nome: str
    idade: int
    data_nascimento: str
    disciplina: str
    salario: float

class UpdateProfessorPayload(BaseModel):
    nome: str
    idade: int
    data_nascimento: str
    disciplina: str
    salario: float

class CreateTurmaPayload(BaseModel):
    id: int
    nome: str
    turno: str
    professor_id: int

class UpdateTurmaPayload(BaseModel):
    nome: str
    turno: str
    professor_id: int