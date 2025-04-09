
from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from spec.payloads import CreateAlunoPayload, UpdateAlunoPayload
from alunos.alunos_models import ModelAlunos

alunos_blueprint = Blueprint('aluno', __name__)

# Rota GET todos os alunos
@alunos_blueprint.route("/alunos", methods=["GET"])
def get_alunos():
    response = ModelAlunos().get_alunos()
    if not response:
        return jsonify(msg="nenhum aluno cadastrado"), 200
    return jsonify(response), 200


# Rota GET aluno por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id: int):
    response = ModelAlunos().get_aluno_by_id(id)
    if not response:
        return jsonify(error='aluno não encontrado'), 404
    return jsonify(response), 200


# Rota POST aluno
@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
    novo_aluno = request.get_json()

    try:
        CreateAlunoPayload(**novo_aluno)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400
    
    response = ModelAlunos().post_aluno(novo_aluno)

    if response.get('error'):
        return jsonify({"error": response['error']}), response['status_code']

    return jsonify(msg=response['msg']), 200

# Rota DELETE aluno por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id: int):

    response = ModelAlunos().delete_aluno(id)

    if not response:
        return jsonify(error="aluno não encontrado para deletagem"), 404

    return jsonify(msg="aluno deletado com sucesso"), 200


# Rota UPDATE alunos por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["PUT"])
def update_aluno(id: int):

    aluno_atualizado = request.get_json()

    try:
        UpdateAlunoPayload(**aluno_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    response = ModelAlunos().update_aluno(id, aluno_atualizado)

    if response.get('error'):
        return jsonify({"error": response["error"]}), 404
    
    return jsonify(response), 200