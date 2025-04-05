from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from spec.payloads import (
    CreateProfessorPayload,
    UpdateProfessorPayload,
)

professores_blueprint = Blueprint('prefessor', __name__)

# Rotas Professor GET

@professores_blueprint.route("/professores", methods=["GET"])
def get_professores():
    if not professores:
        return jsonify(msg="nenhum professor cadastrado"), 200

    return jsonify(professores), 200


# GET Professor por ID


@professores_blueprint.route("/professores/<int:id>", methods=["GET"])
def get_professor(id: int):
    for professor in professores:
        if professor["id"] == id:
            return jsonify(professor), 200

    return jsonify(error="professor não encontrado"), 400


# Rota professor POST


@professores_blueprint.route("/professores", methods=["POST"])
def create_professores():
    novo_professor = request.get_json()

    try:
        CreateProfessorPayload(**novo_professor)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    ids_professores = [professor["id"] for professor in professores]

    if novo_professor["id"] in ids_professores:
        return jsonify(error="id do professor já utilizado"), 400

    professores.append(novo_professor)
    return jsonify(msg="professor cadastrado com sucesso"), 200


# Rota DELETE professor por ID


@professores_blueprint.route("/professores/<int:id>", methods=["DELETE"])
def delete_professores(id: int):

    for professor in professores:
        if professor["id"] == id:
            professores.remove(professor)
            return jsonify(msg="professor removido com sucesso"), 200

    return jsonify(error="professor não encontrado para deletagem"), 400


# Rota UPDATE professor por ID


@professores_blueprint.route("/professores/<int:id>", methods=["PUT"])
def update_professor(id: int):

    professor_atualizado = request.get_json()

    try:
        UpdateProfessorPayload(**professor_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    for index, professor in enumerate(professores):
        if professor.get("id") == id:
            professor_atualizado["id"] = id
            professores[index] = professor_atualizado
            return jsonify(msg="professor atualizado com sucesso"), 200

    return jsonify(error="professor não encontrado para atualização"), 400

