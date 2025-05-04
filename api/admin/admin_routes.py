from flask import jsonify, Blueprint
from admin.admin_models import ModelAdmin
from flasgger import swag_from
from docs_api.admin import reseta_doc

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route("/reseta", methods=["PUT"])
@swag_from(reseta_doc)
def resetar_servidor():
    ModelAdmin().resetar()
    return jsonify(msg="banco de dados esvaziado com sucesso"), 200