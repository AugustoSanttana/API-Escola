from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from spec.payloads import CreateProfessorPayload, UpdateProfessorPayload
from professores.professores_models import ModelProfessores

professores_blueprint = Blueprint('prefessores', __name__)


# Rotas Professor GET


@professores_blueprint.route("/professores", methods=["GET"])
def get_professores():
    response = ModelProfessores().get_professores()
    if not response:
        return jsonify(msg="nenhum professor cadastrado"), 200
    return jsonify(response), 200


# GET Professor por ID
@professores_blueprint.route("/professores/<int:id>", methods=["GET"])
def get_professor(id: int):
    response = ModelProfessores().get_professores_by_id(id)
    if not response:
        return jsonify(error='professor não encontrado'), 400
    return jsonify(response), 200


# Rota professor POST
@professores_blueprint.route("/professores", methods=["POST"])
def create_professores():
    novo_professor = request.get_json()

    try:
        CreateProfessorPayload(**novo_professor)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400
    
    response = ModelProfessores().post_professor(novo_professor) 
    
    if response.get('error'):
        return jsonify({"error": response['error']}), response['status_code']

    return jsonify(msg=response['msg']),200


# Rota DELETE professor por ID


@professores_blueprint.route("/professores/<int:id>", methods=["DELETE"])
def delete_professores(id: int):
    response = ModelProfessores().delete_professor(id)

    if not response:
        return jsonify(error="professor não encontrado para deletagem"), 400

    return jsonify(msg="professor deletado com sucesso"),200
    #return jsonify(msg="professor removido com sucesso"),200

# Rota UPDATE professor por ID


@professores_blueprint.route("/professores/<int:id>", methods=["PUT"])
def update_professor(id: int):

    professor_atualizado = request.get_json()

    try:
        UpdateProfessorPayload(**professor_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    response = ModelProfessores().update_professor(id, professor_atualizado)
   
    if response.get('error'):
       return jsonify({"error": response["error"]}),404
   
    return jsonify(response), 200
       