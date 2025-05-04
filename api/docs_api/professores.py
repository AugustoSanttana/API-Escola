get_professores_doc = {
    "summary": "GET Todos os professores",
    "tags": ["Professores"],
    "responses": {
        "204": {
            "description": "Caso não tenha nenhum professor cadastrado",
            "examples": {"application/json": {"msg": "nenhum professor encontrado"}},
        },
        "200": {
            "description": "Retorna uma lista de professores",
            "examples": {
                "application/json": [
                    {
                        "id": 1,
                        "idade": 40,
                        "materia": "Matemática",
                        "nome": "Ana Souza",
                        "observacoes": "Especialista em álgebra e geometria",
                    },
                    {
                        "id": 2,
                        "idade": 35,
                        "materia": "Física",
                        "nome": "Carlos Pereira",
                        "observacoes": "Tem experiência em laboratório e experimentos práticos",
                    },
                ]
            },
        },
    },
}

get_professor_by_id_doc = {
    "summary": "GET Professor por ID",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID do professor",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Retorna um dicionário com as informações do professor",
            "examples": {
                "application/json": {
                    "id": 1,
                    "idade": 40,
                    "materia": "Matemática",
                    "nome": "Ana Souza",
                    "observacoes": "Especialista em álgebra e geometria",
                }
            },
        },
        "404": {
            "description": "Caso professor não seja encontrado",
            "examples": {"application/json": {"error": "professor não encontrado"}},
        },
    },
}

create_professor_doc = {
    "summary": "POST Professor",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": "Informações do professor",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "idade": {"type": "integer"},
                    "materia": {"type": "string"},
                    "observacoes": {
                        "type": "string",
                    },
                },
                "example": {
                    "nome": "joao",
                    "idade": 23,
                    "materia": "Matemática",
                    "observacoes": "Formado",
                },
            },
        }
    ],
    "responses": {
        "201": {
            "description": "Caso o professor seja cadastrado",
            "examples": {
                "application/json": {"msg": "professor cadastrado com sucesso"}
            },
        },
        "400": {
            "description": "Caso não passe pela validação dos dados",
            "examples": {"application/json": {"error": "payload inválido!"}},
        },
    },
}

delete_professor_by_id_doc = {
    "summary": "DELETE Professor por ID",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID do professor",
            "required": True,
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Deleta o professor",
            "examples": {"application/json": {"msg": "professor deletado com sucesso"}},
        },
        "404": {
            "description": "Caso professor não seja encontrado",
            "examples": {
                "application/json": {"error": "professor não encontrado para deletagem"}
            },
        },
    },
}

update_professor_doc = {
    "summary": "PUT Professor",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "description": "ID do professor",
            "required": True,
            "schema": {"type": "string"},
        },
        {
            "name": "body",
            "in": "body",
            "description": "Informações do professor",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "idade": {"type": "integer"},
                    "materia": {"type": "string"},
                    "observacoes": {
                        "type": "string",
                    },
                },
                "example": {
                    "nome": "joao",
                    "idade": 23,
                    "materia": "Matemática",
                    "observacoes": "Especialista em Algebra",
                },
            },
        },
    ],
    "responses": {
        "200": {
            "description": "Professor atualizado com sucesso",
            "examples": {
                "application/json": {"msg": "professor atualizado com sucesso"}
            },
        },
        "404": {
            "description": "Caso o professor não seja encontrado para atualização",
            "examples": {
                "application/json": {"error": "professor não encontrado para atualização"}
            },
        },
        "400": {
            "description": "Caso não passe pela validação dos dados",
            "examples": {"application/json": {"error": "payload inválido!"}},
        },
    },
}
