from flask import jsonify, Blueprint
from admin.admin_models import ModelAdmin

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route("/reseta", methods=["PUT"])
def resetar_servidor():
    ModelAdmin().resetar()
    return jsonify(msg="banco de dados esvaziado com sucesso"), 200