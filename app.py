from flask import Flask, jsonify, request
from pydantic import ValidationError
from database import banco_de_dados
from spec.payloads import (
    CreateAlunoPayload,
    CreateProfessorPayload,
    CreateTurmaPayload,
    UpdateAlunoPayload,
    UpdateProfessorPayload,
    UpdateTurmaPayload,
)

alunos = banco_de_dados["alunos"]
professores = banco_de_dados["professores"]
turmas = banco_de_dados["turmas"]

app = Flask(__name__)

# Rotas


# Rota GET todos os alunos
@app.route("/alunos", methods=["GET"])
def get_alunos():
    if not alunos:
        return jsonify(msg="nenhum aluno cadastrado"), 200

    return jsonify(alunos), 200


# Rota GET aluno por ID
@app.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id: int):

    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno), 200

    return jsonify(error="aluno não encontrado"), 404


# Rota POST aluno
@app.route("/alunos", methods=["POST"])
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
@app.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id: int):

    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify(msg="aluno deletado com sucesso"), 200

    return jsonify(error="aluno não encontrado para deletagem"), 404


# Rota UPDATE alunos por ID
@app.route("/alunos/<int:id>", methods=["PUT"])
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
        if aluno.get('id') == id:
            aluno_atualizado["id"] = id
            alunos[index] = aluno_atualizado
            return jsonify(msg="aluno atualizado com sucesso"), 200

    return jsonify(error="aluno não encontrado para atualização"), 404


# Rotas Professor GET


@app.route("/professores", methods=["GET"])
def get_professores():
    if not professores:
        return jsonify(msg="nenhum professor cadastrado"), 200

    return jsonify(professores), 200


# GET Professor por ID


@app.route("/professores/<int:id>", methods=["GET"])
def get_professor(id: int):
    for professor in professores:
        if professor["id"] == id:
            return jsonify(professor), 200

    return jsonify(error="professor não encontrado"), 400


# Rota professor POST


@app.route("/professores", methods=["POST"])
def create_professores():
    novo_professor = request.get_json()

    try:
        CreateProfessorPayload(**novo_professor)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    ids_professores = [professor["id"] for professor in professores]

    if novo_professor["id"] in ids_professores:
        return jsonify(error="id do professor já utilizado"), 400

    professores.append(novo_professor)
    return jsonify(msg="professor cadastrado com sucesso"), 200


# Rota DELETE professor por ID


@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professores(id: int):

    for professor in professores:
        if professor["id"] == id:
            professores.remove(professor)
            return jsonify(msg="professor removido com sucesso"), 200

    return jsonify(error="professor não encontrado para deletagem"), 400


# Rota UPDATE professor por ID


@app.route("/professores/<int:id>", methods=["PUT"])
def update_professor(id: int):

    professor_atualizado = request.get_json()

    try:
        UpdateProfessorPayload(**professor_atualizado)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    for index, professor in enumerate(professores):
        if professor.get('id') == id:
            professor_atualizado["id"] = id
            professores[index] = professor_atualizado
            return jsonify(msg="professor atualizado com sucesso"), 200

    return jsonify(error="professor não encontrado para atualização"), 400


# Rota GET para Turma


@app.route("/turmas", methods=["GET"])
def get_turmas():
    if not turmas:
        return jsonify(msg="nenhuma turma cadastrada"), 200

    return jsonify(turmas), 200


# Rota GET turmas por ID
@app.route("/turmas/<int:id>", methods=["GET"])
def get_turma(id: int):

    for turma in turmas:
        if turma["id"] == id:
            return jsonify(turma), 200

    return jsonify(error="turma não encontrada"), 404


# Rota POST Turma


@app.route("/turmas", methods=["POST"])
def create_turma():
    nova_turma = request.get_json()

    try:
        CreateTurmaPayload(**nova_turma)
    except ValidationError:
        return jsonify(error="payload inválido!"), 400

    ids_turmas = [turma["id"] for turma in turmas]
    ids_professores = [professor["id"] for professor in professores]

    if nova_turma["id"] in ids_turmas:
        return jsonify(error="id da turma já existente"), 409

    if nova_turma["professor_id"] not in ids_professores:
        return jsonify(error="professor não existe"), 404

    turmas.append(nova_turma)
    return jsonify(msg="turma cadastrada com sucesso"), 201


# Rota DELETE Turmas por ID
@app.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id: int):

    for turma in turmas:
        if turma["id"] == id:
            turmas.remove(turma)
            return jsonify(msg="turma deletada com sucesso"), 200

    return jsonify(error="turma não encontrada para deletagem"), 404


# Rota UPDATE Turmas por ID
@app.route("/turmas/<int:id>", methods=["PUT"])
def update_turma(id: int):

    turma_atualizada = request.get_json()

    try:
        UpdateTurmaPayload(**turma_atualizada)
    except ValidationError:
        return jsonify(error="payload inválido"), 400

    for index, turma in enumerate(turmas):
        if turma.get("id") == id:
            turma_atualizada["id"] = id
            turmas[index] = turma_atualizada
            return jsonify(msg="turma atualizada com sucesso"), 200

    return jsonify(error="turma não encontrada para atualização"), 404


@app.route("/reseta", methods=["PUT"])
def resetar_servidor():
    turmas.clear()
    alunos.clear()
    professores.clear()
    return jsonify(msg="banco de dados esvaziado com sucesso"), 200


if __name__ == "__main__":
    app.run(debug=False, port=8000)
