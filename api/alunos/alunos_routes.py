
from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from spec.payloads import AlunoPayload
from alunos.alunos_models import ModelAlunos
from flasgger import swag_from
from docs_api.alunos import (
    get_alunos_doc,
    get_aluno_by_id_doc,
    create_aluno_doc,
    delete_aluno_by_id_doc,
    update_aluno_by_id_doc
)

alunos_blueprint = Blueprint('aluno', __name__)

# Rota GET todos os alunos
@alunos_blueprint.route("/alunos", methods=["GET"])
@swag_from(get_alunos_doc)
def get_alunos():
    response = ModelAlunos().get_alunos()
    if not response:
        return jsonify(msg="nenhum aluno cadastrado"), 404
    return jsonify(response), 200


# Rota GET aluno por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["GET"])
@swag_from(get_aluno_by_id_doc)
def get_aluno(id: int):
    response = ModelAlunos().get_aluno_by_id(id)
    if not response:
        return jsonify(error='aluno não encontrado'), 404
    return jsonify(response), 200


# Rota POST aluno
@alunos_blueprint.route("/alunos", methods=["POST"])
@swag_from(create_aluno_doc)
def create_aluno():
    novo_aluno = request.get_json()

    try:
        AlunoPayload(**novo_aluno)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400
    
    response = ModelAlunos().post_aluno(novo_aluno)

    if response.get('error'):
        return jsonify({"error": response['error']}), response['status_code']

    return jsonify(msg=response['msg']), 200

# Rota DELETE aluno por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["DELETE"])
@swag_from(delete_aluno_by_id_doc)
def delete_aluno(id: int):

    response = ModelAlunos().delete_aluno(id)

    if not response:
        return jsonify(error="aluno não encontrado para deletagem"), 404

    return jsonify(msg="aluno deletado com sucesso"), 200


# Rota UPDATE alunos por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["PUT"])
@swag_from(update_aluno_by_id_doc)
def update_aluno(id: int):

    aluno_atualizado = request.get_json()

    try:
        AlunoPayload(**aluno_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    response = ModelAlunos().update_aluno(id, aluno_atualizado)

    if response.get('error'):
        return jsonify({"error": response["error"]}), 404
    
    return jsonify(response), 200