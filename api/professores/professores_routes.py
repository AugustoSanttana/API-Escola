from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from spec.payloads import ProfessorPayload
from professores.professores_models import ModelProfessores
from flasgger import swag_from
from docs_api.professores import (
    create_professor_doc,
    delete_professor_by_id_doc,
    get_professor_by_id_doc,
    get_professores_doc,
    update_professor_doc
)

professores_blueprint = Blueprint('prefessores', __name__)


# Rota Professor GET
@professores_blueprint.route("/professores", methods=["GET"])
@swag_from(get_professores_doc)
def get_professores():
    response = ModelProfessores().get_professores()
    if not response:
        return jsonify(msg="nenhum professor encontrado"), 200
    return jsonify(response), 200


# GET Professor por ID
@professores_blueprint.route("/professores/<int:id>", methods=["GET"])
@swag_from(get_professor_by_id_doc)
def get_professor(id: int):
    response = ModelProfessores().get_professores_by_id(id)
    if not response:
        return jsonify(error='professor não encontrado'), 404
    return jsonify(response), 200


# Rota professor POST
@professores_blueprint.route("/professores", methods=["POST"])
@swag_from(create_professor_doc)
def create_professores():
    novo_professor = request.get_json()

    try:
        ProfessorPayload(**novo_professor)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400
    
    response = ModelProfessores().post_professor(novo_professor) 
    return jsonify(msg=response['msg']), 201


# Rota DELETE professor por ID
@professores_blueprint.route("/professores/<int:id>", methods=["DELETE"])
@swag_from(delete_professor_by_id_doc)
def delete_professores(id: int):
    response = ModelProfessores().delete_professor(id)

    if not response:
        return jsonify(error="professor não encontrado para deletagem"), 400

    return jsonify(msg="professor deletado com sucesso"),200

# Rota UPDATE professor por ID
@professores_blueprint.route("/professores/<int:id>", methods=["PUT"])
@swag_from(update_professor_doc)
def update_professor(id: int):

    professor_atualizado = request.get_json()

    try:
        ProfessorPayload(**professor_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    response = ModelProfessores().update_professor(id, professor_atualizado)
   
    if response.get('error'):
       return jsonify({"error": response["error"]}),404
   
    return jsonify(response), 200
       