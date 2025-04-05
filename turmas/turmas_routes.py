from pydantic import ValidationError
from flask import jsonify, request, Blueprint
from spec.payloads import (
    CreateTurmaPayload,
    UpdateTurmaPayload,
)

turmas_blueprint = Blueprint('turma', __name__)

# Rota GET para Turma


@turmas_blueprint.route("/turmas", methods=["GET"])
def get_turmas():
    if not turmas:
        return jsonify(msg="nenhuma turma cadastrada"), 200

    return jsonify(turmas), 200


# Rota GET turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["GET"])
def get_turma(id: int):

    for turma in turmas:
        if turma["id"] == id:
            return jsonify(turma), 200

    return jsonify(error="turma não encontrada"), 404


# Rota POST Turma


@turmas_blueprint.route("/turmas", methods=["POST"])
def create_turma():
    nova_turma = request.get_json()

    try:
        CreateTurmaPayload(**nova_turma)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    ids_turmas = [turma["id"] for turma in turmas]
    ids_professores = [professor["id"] for professor in professores]

    if nova_turma["id"] in ids_turmas:
        return jsonify(error="id da turma já existente"), 409

    if nova_turma["professor_id"] not in ids_professores:
        return jsonify(error="professor não existe"), 404

    turmas.append(nova_turma)
    return jsonify(msg="turma cadastrada com sucesso"), 201


# Rota DELETE Turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id: int):

    for turma in turmas:
        if turma["id"] == id:
            turmas.remove(turma)
            return jsonify(msg="turma deletada com sucesso"), 200

    return jsonify(error="turma não encontrada para deletagem"), 404


# Rota UPDATE Turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["PUT"])
def update_turma(id: int):

    turma_atualizada = request.get_json()

    try:
        UpdateTurmaPayload(**turma_atualizada)
    except ValidationError:
        return jsonify(error="payload inválido"), 400

    for index, turma in enumerate(turmas):
        if turma.get("id") == id:
            turma_atualizada["id"] = id
            turmas[index] = turma_atualizada
            return jsonify(msg="turma atualizada com sucesso"), 200

    return jsonify(error="turma não encontrada para atualização"), 404
