import pytest
from app import app
from database import DatabaseManager

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def created_professor(client):
    # Cria um professor antes dos testes de atualização e exclusão
    response = client.post("/professores", json={
        "nome": "Professor Teste",
        "idade": 45,
        "materia": "Biologia",
        "observacoes": "Especialista em botânica"
    })
    assert response.status_code == 201
    return response.json.get("id")  # Retorna o ID do professor criado

# Testes para alunos
def test_get_alunos(client):
    response = client.get("/alunos")
    if response.status_code == 404:
        assert response.json["msg"] == "nenhum aluno cadastrado"
    else:
        assert response.status_code == 200
        assert isinstance(response.json, list)

def test_get_aluno_por_id(client):
    response = client.get("/alunos/1")
    if response.status_code == 200:
        assert "nome" in response.json
    else:
        assert response.status_code == 404
        assert response.json["error"] == "aluno não encontrado"

def test_create_aluno(client):
    novo_aluno = {
        "nome": "NovoAluno",
        "idade": 12,
        "data_nascimento": "2012-05-14",
        "nota_primeiro_semestre": 9.0,
        "nota_segundo_semestre": 8.0,
        "turma_id": 1,
    }

    response = client.post("/alunos", json=novo_aluno)
    if response.status_code == 404:
        assert response.json["error"] == "turma não existe"
    else:
        assert response.status_code == 200
        assert response.json["msg"] == "aluno cadastrado com sucesso"

def test_delete_aluno(client):
    response = client.delete("/alunos/1")
    if response.status_code == 200:
        assert response.json["msg"] == "aluno deletado com sucesso"
    else:
        assert response.status_code == 404
        assert response.json["error"] == "aluno não encontrado para deletagem"

def test_update_aluno(client):
    aluno_atualizado = {
        "nome": "Aluno Atualizado",
        "idade": 13,
        "data_nascimento": "2011-06-15",
        "nota_primeiro_semestre": 8.5,
        "nota_segundo_semestre": 7.5,
        "turma_id": 1,
    }

    response = client.put("/alunos/1", json=aluno_atualizado)
    if response.status_code == 404:
        assert "error" in response.json
        assert response.json["error"] in ["aluno não encontrado para atualização", "turma não existe"]
    else:
        assert response.status_code == 200
        assert response.json["msg"] == "aluno atualizado com sucesso"

def test_create_professor(client):
    novo_professor = {
        "nome": "Professor Teste",
        "idade": 40,
        "materia": "História",
        "observacoes": "Professor temporário"
    }

    response = client.post("/professores", json=novo_professor)
    assert response.status_code == 201
    assert response.json["msg"] == "professor cadastrado com sucesso"

def test_get_professores(client):
    response = client.get("/professores")
    assert response.status_code == 200
    assert isinstance(response.json, list) or "msg" in response.json  # pode não haver professores

def test_get_professor_por_id(client):
    # Criar um professor para garantir que exista
    professor = {
        "nome": "Professor A",
        "idade": 45,
        "materia": "Matemática",
        "observacoes": "Efetivo"
    }
    client.post("/professores", json=professor)

    # Verifica se retorna corretamente
    response = client.get("/professores/1")
    if response.status_code == 200:
        assert "nome" in response.json
    else:
        assert response.status_code == 404
        assert response.json["error"] == "professor não encontrado"

def test_update_professor(client):
    professor_atualizado = {
        "nome": "Professor Atualizado",
        "idade": 50,
        "materia": "Física",
        "observacoes": "Coordenador"
    }

    response = client.put("/professores/1", json=professor_atualizado)
    if response.status_code == 200:
        assert response.json["msg"] == "professor atualizado com sucesso"
    else:
        assert response.status_code == 404
        assert response.json["error"] == "professor não encontrado para atualização"

def test_delete_professor(client):
    response = client.delete("/professores/1")
    if response.status_code == 200:
        assert response.json["msg"] == "professor deletado com sucesso"
    else:
        assert response.status_code == 400
        assert response.json["error"] == "professor não encontrado para deletagem"

def test_create_turma(client):
    nova_turma = {
        "descricao": "Turma Teste",
        "professor_id": 2,
        "ativo": True
    }
    response = client.post("/turmas", json=nova_turma)
    assert response.status_code == 201

# Teste de busca de todas as turmas
def test_get_turmas(client):
    response = client.get("/turmas")
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Teste de busca de turma por ID
def test_get_turma_por_id(client):
    response = client.get("/turmas/1")
    if response.status_code == 200:
        assert "descricao" in response.json
    else:
        assert response.status_code == 404
        assert response.json["error"] == "turma não encontrada"

# Teste de deletar turma
def test_delete_turma(client):
    # Cria uma turma para garantir que o ID exista
    nova_turma = {
        "descricao": "Turma Para Deletar",
        "professor_id": 2,
        "ativo": True
    }
    client.post("/turmas", json=nova_turma)

    # Assume que a turma criada tenha o ID 1 (ajuste conforme necessário)
    response = client.delete("/turmas/1")
    assert response.status_code == 200
    assert response.json["msg"] == "turma deletada com sucesso"

    # Verifica se foi realmente deletada
    response = client.get("/turmas/1")
    assert response.status_code == 404
    assert response.json["error"] == "turma não encontrada"

# Teste de atualização de turma
def test_update_turma(client):
    # Cria turma antes para atualizar
    turma = {
        "descricao": "Turma Atualizar",
        "professor_id": 1,
        "ativo": True
    }
    client.post("/turmas", json=turma)

    turma_atualizada = {
        "descricao": "Turma Atualizada com Sucesso",
        "professor_id": 1,
        "ativo": False
    }
    response = client.put("/turmas/3", json=turma_atualizada)
    if response.status_code == 200:
        assert response.json["msg"] == "turma atualizada com sucesso"
    else:
        assert response.status_code == 404
        assert "error" in response.json
