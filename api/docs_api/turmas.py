get_turmas_doc = {
    "summary": "GET Todas as turmas",
    "tags": ["Turmas"],
    "responses": {
        "204": {
            "description": "Caso não tenha nenhuma turma cadastrada",
            "examples": {"application/json": {"msg": "nenhuma turma cadastrada"}},
        },
        "200": {
            "description": "Lista as turmas cadastradas",
            "examples": {
                "application/json": [
                    {
                        "ativo": "true",
                        "descricao": "Matemática",
                        "id": 2,
                        "professor_id": 1,
                    },
                    {"ativo": "true", "descricao": "Inglês", "id": 1, "professor_id": 3},
                ]
            },
        },
    },
}

get_turma_by_id_doc = {
    "summary": "GET Turma por ID",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID da turma",
            "required": True,
            "schema": {"type": "integer"},
        }
    ],
    "responses": {
        "200": {
            "description": "Retorna as informações da turma",
            "examples": {
                "application/json": {
                    "id": 1,
                    "descricao": "Turma A - Manhã",
                    "professor_id": 2,
                    "ativo": True,
                }
            },
        },
        "404": {
            "description": "Caso a turma não seja encontrada",
            "examples": {"application/json": {"error": "turma não encontrada"}},
        },
    },
}

create_turma_doc = {
    "summary": "POST Turma",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Informações da nova turma",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "descricao": {"type": "string"},
                    "professor_id": {"type": "integer"},
                    "ativo": {"type": "boolean"},
                },
                "example": {
                    "descricao": "Turma C - Noite",
                    "professor_id": 1,
                    "ativo": True,
                },
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Turma cadastrada com sucesso",
            "examples": {"application/json": {"msg": "turma cadastrada com sucesso"}},
        },
        "400": {
            "description": "Payload inválido",
            "examples": {"application/json": {"error": "payload inválido!"}},
        },
        "404": {
            "description": "Professor não encontrado",
            "examples": {"application/json": {"error": "professor não existe"}},
        },
    },
}

delete_turma_doc = {
    "summary": "DELETE Turma por ID",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID da turma a ser deletada",
            "required": True,
            "schema": {"type": "integer"},
        }
    ],
    "responses": {
        "200": {
            "description": "Turma deletada com sucesso",
            "examples": {"application/json": {"msg": "turma deletada com sucesso"}},
        },
        "404": {
            "description": "Turma não encontrada para deletagem",
            "examples": {
                "application/json": {"error": "turma não encontrada para deletagem"}
            },
        },
    },
}

update_turma_doc = {
    "summary": "PUT Atualizar Turma",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID da turma a ser atualizada",
            "required": True,
            "schema": {"type": "integer"},
        },
        {
            "name": "body",
            "in": "body",
            "description": "Novas informações da turma",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "descricao": {"type": "string"},
                    "professor_id": {"type": "integer"},
                    "ativo": {"type": "boolean"},
                },
                "example": {
                    "descricao": "Turma D - Tarde",
                    "professor_id": 3,
                    "ativo": False,
                },
            },
        },
    ],
    "responses": {
        "200": {
            "description": "Turma atualizada com sucesso",
            "examples": {"application/json": {"msg": "turma atualizada com sucesso"}},
        },
        "400": {
            "description": "Payload inválido",
            "examples": {"application/json": {"error": "payload inválido"}},
        },
        "404": {
            "description": "Erro ao atualizar (turma ou professor não encontrado)",
            "examples": {
                "application/json 1": {
                    "error": "turma não encontrada para atualização"
                },
                "application/json 2": {"error": "id professor não existe"},
            },
        },
        "404": {
            "description": "Erro ao atualizar, caso professor não seja encontrado",
            "examples": {
                "application/json": {"error": "id professor não existe"},
            },
        }
    },
}
