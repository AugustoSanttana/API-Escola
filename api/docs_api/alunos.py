get_alunos_doc = {
    "summary": "GET Todos os alunos",
    "tags": ["Alunos"],
    "responses": {
        "404": {
            "description": "Caso não tenha nenhum aluno cadastrado",
            "examples": {"application/json": {"msg": "nenhum aluno encontrado"}},
        },
        "200": {
            "description": "Retorna uma lista de alunos",
            "examples": {
                "application/json": [
                    {
                        "data_nascimento": "Wed, 22 Mar 2006 00:00:00 GMT",
                        "id": 1,
                        "idade": 18,
                        "media_final": 7.75,
                        "nome": "Alice Martins",
                        "nota_primeiro_semestre": 8.0,
                        "nota_segundo_semestre": 7.5,
                        "turma_id": 1,
                    },
                    {
                        "data_nascimento": "Sun, 15 Apr 2007 00:00:00 GMT",
                        "id": 2,
                        "idade": 17,
                        "media_final": 7.0,
                        "nome": "Gabriel Silva",
                        "nota_primeiro_semestre": 7.2,
                        "nota_segundo_semestre": 6.8,
                        "turma_id": 1,
                    },
                ]
            },
        },
    },
}
get_aluno_by_id_doc = {
    "summary": "GET Aluno por ID",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID do aluno",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Retorna um dicionário com as informações do aluno",
            "examples": {
                "application/json": {
                    "data_nascimento": "Sun, 10 Jun 2007 00:00:00 GMT",
                    "id": 5,
                    "idade": 17,
                    "media_final": 9.1,
                    "nome": "Letícia Costa",
                    "nota_primeiro_semestre": 9.0,
                    "nota_segundo_semestre": 9.2,
                    "turma_id": 1,
                }
            },
        },
        "404": {
            "description": "Caso aluno não seja encontrado",
            "examples": {"application/json": {"error": "aluno não encontrado"}},
        },
    },
}

create_aluno_doc = {
    "summary": "POST Aluno",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Informações do aluno",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "idade": {"type": "integer"},
                    "turma_id": {"type": "integer"},
                    "data_nascimento": {"type": "string", "format": "date"},
                    "nota_primeiro_semestre": {"type": "number", "format": "float"},
                    "nota_segundo_semestre": {"type": "number", "format": "float"},
                },
                "example": {
                    "nome": "Carlos",
                    "idade": 20,
                    "turma_id": 2,
                    "data_nascimento": "2005-03-15",
                    "nota_primeiro_semestre": 7.5,
                    "nota_segundo_semestre": 8.0,
                },
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Caso o aluno seja cadastrado",
            "examples": {"application/json": {"msg": "aluno cadastrado com sucesso"}},
        },
        "400": {
            "description": "Caso não passe pela validação dos dados",
            "examples": {"application/json": {"error": "payload inválido!"}},
        },
        "404": {
            "description": "Caso o campo turma_id não for válido",
            "examples": {"application/json": {"error": "turma não existe"}},
        },
    },
}

delete_aluno_by_id_doc = {
    "summary": "DELETE Aluno por ID",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID do aluno",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Deleta o aluno",
            "examples": {"application/json": {"msg": "aluno deletado com sucesso"}},
        },
        "404": {
            "description": "Caso aluno não seja encontrado",
            "examples": {
                "application/json": {"error": "aluno não encontrado para deletagem"}
            },
        },
    },
}

update_aluno_by_id_doc = {
    "summary": "PUT Aluno por ID",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID do aluno a ser atualizado",
            "required": True,
            "schema": {"type": "integer", "format": "int32"},
        },
        {
            "name": "body",
            "in": "body",
            "description": "Dados do aluno a serem atualizados",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "idade": {"type": "integer"},
                    "turma_id": {"type": "integer"},
                    "data_nascimento": {"type": "string", "format": "date"},
                    "nota_primeiro_semestre": {"type": "number", "format": "float"},
                    "nota_segundo_semestre": {"type": "number", "format": "float"},
                },
                "example": {
                    "nome": "Carlos",
                    "idade": 20,
                    "turma_id": 2,
                    "data_nascimento": "2005-03-15",
                    "nota_primeiro_semestre": 7.5,
                    "nota_segundo_semestre": 8.0,
                },
            },
        },
    ],
    "responses": {
        "200": {
            "description": "Aluno atualizado com sucesso",
            "examples": {"application/json": {"msg": "aluno atualizado com sucesso"}},
        },
        "404": {
            "description": "Caso o aluno não seja encontrado para atualização",
            "examples": {
                "application/json": {"error": "aluno não encontrado para atualização"}
            },
        },
        "400": {
            "description": "Caso não passe pela validação dos dados",
            "examples": {"application/json": {"error": "payload inválido!"}},
        },
    },
}
