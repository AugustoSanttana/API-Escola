import pytest
from app import app

#rodar o comando: "pytest tests.py -vv" para executar os testes automatizados#

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Testes
def test_get_alunos(client):
    response = client.get("/alunos")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_aluno_por_id(client):
    response = client.get("/alunos/1")
    assert response.status_code == 200
    assert response.json["nome"] == "ExemploAluno1"

    response = client.get("/alunos/999")
    assert response.status_code == 404
    assert response.json["error"] == "aluno não encontrado"


def test_create_aluno(client):
    novo_aluno = {
        "id": 3,
        "nome": "NovoAluno",
        "idade": 12,
        "data_nascimento": "(2012/05/14)",
        "nota_primeiro_semestre": 9.0,
        "nota_segundo_semestre": 8.0,
        "media_final": 8.5,
        "turma_id": 2,
    }

    response = client.post("/alunos", json=novo_aluno)
    assert response.status_code == 200
    assert response.json["msg"] == "aluno cadastrado com sucesso"

    response = client.get("/alunos/3")
    assert response.status_code == 200
    assert response.json["nome"] == "NovoAluno"


def test_delete_aluno(client):
    response = client.delete("/alunos/2")
    assert response.status_code == 200
    assert response.json["msg"] == "aluno deletado com sucesso"

    response = client.get("/alunos/2")
    assert response.status_code == 404
    assert response.json["error"] == "aluno não encontrado"


def test_update_aluno(client):
    aluno_atualizado = {
        "nome": "ExemploAluno1 Atualizado",
        "idade": 12,
        "data_nascimento": "(2012/03/18)",
        "nota_primeiro_semestre": 9.5,
        "nota_segundo_semestre": 8.5,
        "media_final": 9.0,
        "turma_id": 1,
    }

    response = client.put("/alunos/1", json=aluno_atualizado)
    assert response.status_code == 200
    assert response.json["msg"] == "aluno atualizado com sucesso"

    response = client.get("/alunos/1")
    assert response.status_code == 200
    assert response.json["nome"] == "ExemploAluno1 Atualizado"


def test_get_professores(client):
    response = client.get("/professores")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_professor_por_id(client):
    response = client.get("/professores/1")
    assert response.status_code == 200
    assert response.json["nome"] == "Tonho"

    response = client.get("/professores/999")
    assert response.status_code == 400
    assert response.json["error"] == "professor não encontrado"


def test_update_professor(client):
    professor_atualizado = {
        "nome": "Tonho Atualizado",
        "idade": 45,
        "data_nascimento": "(1979/07/23)",
        "disciplina": "Matemática Avançada",
        "salario": 3000.00,
    }

    response = client.put("/professores/1", json=professor_atualizado)
    assert response.status_code == 200
    assert response.json["msg"] == "professor atualizado com sucesso"

    response = client.get("/professores/1")
    assert response.status_code == 200
    assert response.json["nome"] == "Tonho Atualizado"


def test_delete_professor(client):
    response = client.delete("/professores/2")
    assert response.status_code == 200
    assert response.json["msg"] == "professor deletado com sucesso"

    response = client.delete("/professores/2")
    assert response.status_code == 400
    assert response.json["error"] == "professor não encontrado para deletagem"


def test_create_professor(client):
    novo_professor = {
        "id": 3,
        "nome": "NovoProfessor",
        "idade": 35,
        "data_nascimento": "(1989/02/20)",
        "disciplina": "Geografia",
        "salario": 3000.00,
    }

    response = client.post("/professores", json=novo_professor)
    assert response.status_code == 200
    assert response.json["msg"] == "professor cadastrado com sucesso"


def test_get_turmas(client):
    response = client.get("/turmas")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_turma_por_id(client):
    response = client.get("/turmas/1")
    assert response.status_code == 200
    assert response.json["nome"] == "sexto ano"

    response = client.get("/turmas/999")
    assert response.status_code == 404
    assert response.json["error"] == "turma não encontrada"


def test_create_turma(client):
    nova_turma = {
        "id": 3,
        "nome": "oitavo ano",
        "turno": "Vespertino",
        "professor_id": 1,
    }

    response = client.post("/turmas", json=nova_turma)
    assert response.status_code == 201
    assert response.json["msg"] == "turma cadastrada com sucesso"


def test_delete_turma(client):
    response = client.delete("/turmas/2")
    assert response.status_code == 200
    assert response.json["msg"] == "turma deletada com sucesso"

    response = client.get("/turmas/2")
    assert response.status_code == 404
    assert response.json["error"] == "turma não encontrada"


def test_update_turma(client):

    turma_para_adicionar = {
        "id": 2,
        "nome": "Sétimo Ano",
        "turno": "Matutino",
        "professor_id": 1,
    }

    response = client.post("/turmas", json=turma_para_adicionar)
    assert response.status_code == 201

    turma_atualizada = {
        "nome": "Sétimo Ano A",
        "turno": "Vespertino",
        "professor_id": 1,
    }

    response = client.put("/turmas/2", json=turma_atualizada)
    assert response.status_code == 200
    assert response.json["msg"] == "turma atualizada com sucesso"

    response = client.get("/turmas/2")
    assert response.status_code == 200
    assert response.json["nome"] == "Sétimo Ano A"
    assert response.json["turno"] == "Vespertino"


def test_reset(client):
    
    aluno_para_adicionar = {
        "id": 3,
        "nome": "Aluno Teste",
        "idade": 15,
        "data_nascimento": "(2009/03/18)",
        "nota_primeiro_semestre": 8.5,
        "nota_segundo_semestre": 7.0,
        "media_final": 7.75,
        "turma_id": 1
    }
    professor_para_adicionar = {
        "id": 3,
        "nome": "Professor Teste",
        "idade": 40,
        "data_nascimento": "(1985/06/10)",
        "disciplina": "Geografia",
        "salario": 3500.00
    }
    turma_para_adicionar = {
        "id": 3,
        "nome": "Oitavo Ano",
        "turno": "Vespertino",
        "professor_id": 1
    }

    client.post("/alunos", json=aluno_para_adicionar)
    client.post("/professores", json=professor_para_adicionar)
    client.post("/turmas", json=turma_para_adicionar)

    response = client.get("/alunos")
    assert response.status_code == 200
    assert len(response.json) > 0
    
    response = client.get("/professores")
    assert response.status_code == 200
    assert len(response.json) > 0
    
    response = client.get("/turmas")
    assert response.status_code == 200
    assert len(response.json) > 0
    
    response = client.put("/reseta")
    assert response.status_code == 200
    assert response.json["msg"] == "banco de dados esvaziado com sucesso"
    
    response = client.get("/alunos")
    assert response.status_code == 200
    assert response.json["msg"] == "nenhum aluno cadastrado"
    
    response = client.get("/professores")
    assert response.status_code == 200
    assert response.json["msg"] == "nenhum professor cadastrado"
    
    response = client.get("/turmas")
    assert response.status_code == 200
    assert response.json["msg"] == "nenhuma turma cadastrada"
