
from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from spec.payloads import CreateAlunoPayload, UpdateAlunoPayload

alunos_blueprint = Blueprint('aluno', __name__)

# Rota GET todos os alunos
@alunos_blueprint.route("/alunos", methods=["GET"])
def get_alunos():
    if not alunos:
        return jsonify(msg="nenhum aluno cadastrado"), 200

    return jsonify(alunos), 200


# Rota GET aluno por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id: int):

    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno), 200

    return jsonify(error="aluno não encontrado"), 404


# Rota POST aluno
@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
    novo_aluno = request.get_json()

    try:
        CreateAlunoPayload(**novo_aluno)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    ids_cadastrados = [aluno["id"] for aluno in alunos]
    ids_turmas_cadastradas = [turma["id"] for turma in turmas]

    if novo_aluno["id"] in ids_cadastrados:
        return jsonify(error="id do aluno ja utilizado"), 400

    if novo_aluno["turma_id"] not in ids_turmas_cadastradas:
        return jsonify(error="turma não existe"), 404

    alunos.append(novo_aluno)
    return jsonify(msg="aluno cadastrado com sucesso"), 200


# Rota DELETE aluno por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id: int):

    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify(msg="aluno deletado com sucesso"), 200

    return jsonify(error="aluno não encontrado para deletagem"), 404


# Rota UPDATE alunos por ID
@alunos_blueprint.route("/alunos/<int:id>", methods=["PUT"])
def update_aluno(id: int):

    aluno_atualizado = request.get_json()

    try:
        UpdateAlunoPayload(**aluno_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    ids_turmas_cadastradas = [turma["id"] for turma in turmas]

    if aluno_atualizado["turma_id"] not in ids_turmas_cadastradas:
        return jsonify(error="turma não existe"), 404

    for index, aluno in enumerate(alunos):
        if aluno.get("id") == id:
            aluno_atualizado["id"] = id
            alunos[index] = aluno_atualizado
            return jsonify(msg="aluno atualizado com sucesso"), 200

    return jsonify(error="aluno não encontrado para atualização"), 404












































'''from flask import Blueprint, request, jsonify
from database import banco_de_dados
from pydantic import ValidationError
from .alunos_model import AlunoNaoEncontrado, aluno_por_id, listar_alunos, adicionar_aluno
from spec.payloads import (
    CreateAlunoPayload,
    CreateProfessorPayload,
    CreateTurmaPayload,
    UpdateAlunoPayload,
    UpdateProfessorPayload,
    UpdateTurmaPayload,
)


alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id: int):
  try:
    aluno = aluno_por_id(id)
    return jsonify(aluno)
  except AlunoNaoEncontrado:
    return jsonify(error="aluno não encontrado"), 404
  
@alunos_blueprint.route("/alunos", methods=["GET"])
def get_alunos():
  return jsonify(listar_alunos())

@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
  novo_aluno = request.get_json()
  
  try:
        CreateAlunoPayload(**novo_aluno)
  except ValidationError:
        return jsonify(error="payload inválido!"), 400

  ids_cadastrados = [aluno["id"] for aluno in banco_de_dados["alunos"]]
  ids_turmas_cadastradas = [turma["id"] for turma in banco_de_dados["turmas"]]

  if novo_aluno["id"] in ids_cadastrados:
      return jsonify(error="id do aluno ja utilizado"), 400

  if novo_aluno["turma_id"] not in ids_turmas_cadastradas:
      return jsonify(error="turma não existe"), 404

  banco_de_dados["alunos"].append(novo_aluno)
  return jsonify(msg="aluno cadastrado com sucesso"), 200
'''


  