from flask import jsonify, Blueprint
from database import banco_de_dados
from admin.admin_models import ModelAdmin

alunos = banco_de_dados['alunos']
turmas = banco_de_dados['turmas']
professores = banco_de_dados['professores']

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route("/reseta", methods=["PUT"])
def resetar_servidor():
    ModelAdmin().resetar()
    return jsonify(msg="banco de dados esvaziado com sucesso"), 200