from pydantic import ValidationError
from flask import jsonify, request, Blueprint
from spec.payloads import CreateTurmaPayload, UpdateTurmaPayload
from turmas.turmas_models import ModelTurmas


turmas_blueprint = Blueprint('turma', __name__)

# Rota GET para Turma


@turmas_blueprint.route("/turmas", methods=["GET"])
def get_turmas():
    response = ModelTurmas().get_turmas()
    if not response:
        return jsonify(msg="nenhuma turma cadastrada"), 200
    return jsonify(response), 200


# Rota GET turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["GET"])
def get_turma(id: int):
    response = ModelTurmas().get_turmas_by_id(id)
    if not response:
        return jsonify(error='turma não encontrada'), 404
    return jsonify(response), 200


# Rota POST Turma


@turmas_blueprint.route("/turmas", methods=["POST"])
def create_turma():
    nova_turma = request.get_json()

    try:
        CreateTurmaPayload(**nova_turma)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    response = ModelTurmas().post_turma(nova_turma)

    if response.get('error'):
        return jsonify({"error": response['error']}), response['status_code']

    return jsonify(msg=response['msg']), 201

# Rota DELETE Turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id: int):
    response = ModelTurmas().delete_turma(id)

    if not response:
        return jsonify(error="turma não encontrada para deletagem"), 404
    
    return jsonify(msg="turma deletada com sucesso"), 200


# Rota UPDATE Turmas por ID
@turmas_blueprint.route("/turmas/<int:id>", methods=["PUT"])
def update_turma(id: int):

    turma_atualizada = request.get_json()

    try:
        UpdateTurmaPayload(**turma_atualizada)
    except ValidationError:
        return jsonify(error="payload inválido"), 400

    response = ModelTurmas().update_turma(id, turma_atualizada)

    if response.get('error'):
        return jsonify({"error": response["error"]}), 404
    
    return jsonify(response), 200