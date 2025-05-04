from pydantic import ValidationError
from flask import jsonify, request, Blueprint
from spec.payloads import TurmaPayload
from turmas.turmas_models import ModelTurmas
from flasgger import swag_from
from docs_api.turmas import (
    create_turma_doc,
    delete_turma_doc,
    get_turma_by_id_doc,
    get_turmas_doc,
    update_turma_doc
)


turmas_blueprint = Blueprint('turma', __name__)

# Rota GET para Turma


@turmas_blueprint.route("/turmas", methods=["GET"])
@swag_from(get_turmas_doc)
def get_turmas():
    response = ModelTurmas().get_turmas()
    if not response:
        return jsonify(msg="nenhuma turma cadastrada"), 200
    return jsonify(response), 200


# Rota GET turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["GET"])
@swag_from(get_turma_by_id_doc)
def get_turma(id: int):
    response = ModelTurmas().get_turmas_by_id(id)
    if not response:
        return jsonify(error='turma não encontrada'), 404
    return jsonify(response), 200


# Rota POST Turma


@turmas_blueprint.route("/turmas", methods=["POST"])
@swag_from(create_turma_doc)
def create_turma():
    nova_turma = request.get_json()

    try:
        TurmaPayload(**nova_turma)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    response = ModelTurmas().post_turma(nova_turma)

    if response.get('error'):
        return jsonify({"error": response['error']}), response['status_code']

    return jsonify(msg=response['msg']), 201

# Rota DELETE Turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["DELETE"])
@swag_from(delete_turma_doc)
def delete_turma(id: int):
    response = ModelTurmas().delete_turma(id)

    if not response:
        return jsonify(error="turma não encontrada para deletagem"), 404
    
    return jsonify(msg="turma deletada com sucesso"), 200


# Rota UPDATE Turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["PUT"])
@swag_from(update_turma_doc)
def update_turma(id: int):

    turma_atualizada = request.get_json()

    try:
        TurmaPayload(**turma_atualizada)
    except ValidationError:
        return jsonify(error="payload inválido"), 400

    response = ModelTurmas().update_turma(id, turma_atualizada)

    if response.get('error'):
        return jsonify({"error": response["error"]}), 404
    
    return jsonify(response), 200