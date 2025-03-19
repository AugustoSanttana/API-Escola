from pydantic import BaseModel
from typing import Optional

class CreateAlunoPayload(BaseModel):
    id: int
    nome: str
    data_nascimento: str
    nota_primeiro_semestre: Optional[float] = None
    nota_segundo_semestre: Optional[float] = None
    media_final: Optional[float] = None
    turma_id: int

class UpdateAlunoPayload(BaseModel):
    nome: Optional[str] = None
    data_nascimento: Optional[str] = None
    nota_primeiro_semestre: Optional[float] = None
    nota_segundo_semestre: Optional[float] = None
    media_final: Optional[float] = None
    turma_id: Optional[int] = None

class CreateProfessorPayload(BaseModel):
    id: int
    nome: str
    idade: int
    data_nascimento: str
    disciplina: str
    salario: float

class UpdateProfessorPayload(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    data_nascimento: Optional[str] = None
    disciplina: Optional[str] = None
    salario: Optional[float] = None

class CreateTurmaPayload(BaseModel):
    id: int
    nome: str
    turno: str
    id_professor: int

class UpdateTurmaPayload(BaseModel):
    nome: Optional[str] = None
    turno: Optional[str] = None
    id_professor: Optional[int] = None