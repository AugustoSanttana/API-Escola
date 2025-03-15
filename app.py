from flask import Flask, jsonify, request
from database import banco_de_dados

alunos = banco_de_dados["alunos"]
professores = banco_de_dados["professores"]

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
    print(novo_aluno)

    if not novo_aluno or "id" not in novo_aluno or "nome" not in novo_aluno:
        return jsonify(error="payload inválido"), 400

    ids_cadastrados = [aluno["id"] for aluno in alunos]

    if novo_aluno["id"] in ids_cadastrados:
        return jsonify(error="id já existente"), 409

    alunos.append(novo_aluno)
    return jsonify(msg="aluno cadastrado com sucesso"), 201


# Rota DELETE aluno por ID
@app.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id: int):

    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify(msg="aluno deletado com sucesso"), 200

    return jsonify(error="aluno não encontrado para deletagem"), 404


# Rota UPDATE alunos por ID
@app.route("/alunos/<int:id>", methods=["PATCH"])
def update_aluno(id: int):

    novo_nome_aluno = request.get_json()

    if not novo_nome_aluno or "nome" not in novo_nome_aluno:
        return jsonify(error="payload inválido"), 400

    for aluno in alunos:
        if aluno["id"] == id:
            aluno["nome"] = novo_nome_aluno["nome"]
            return jsonify(msg="nome do aluno atualizado com sucesso"), 200

    return jsonify(error="aluno não encontrado para atualização"), 404


# Rotas Professor GET

@app.route("/professores", methods=["GET"])
def get_professores():
    if not professores: 
        return jsonify(msg="Nenhum professor cadastrado"), 200
    return jsonify(professores), 200

# GET Professor por ID

@app.route("/professores/<int:id>", methods=["GET"])
def get_professor(id: int):
    for professor in professores:
        if professor["id"] == id:
          return jsonify(professor), 200
    
    return jsonify(error="Professor não encontrado"), 404

# Rota professor POST
    
@app.route("/professores", methods=["POST"])
def create_professores():
    novo_professor = request.get_json()
    print(novo_professor)

    if not novo_professor or "id" not in novo_professor or "nome" not in novo_professor:
        return jsonify(error="payload inválido"), 400

    ids_professores = [professor["id"] for professor in professores]

    if novo_professor["id"] in ids_professores:
        return jsonify(error="id já existente"), 409

    professores.append(novo_professor)
    return jsonify(msg="professor cadastrado com sucesso"), 201

# Rota DELETE professor por ID

@app.route("/professores/<int:id>", methods= ["DELETE"])
def delete_professores(id: int):
    
    for professor in professores:
        if professor["id"] == id:
            professores.remove(professor)
            return jsonify(msg= "Professor removido com sucesso"), 200
    
    return jsonify(error="Professor não encontrado para deletagem"), 404

# Rota UPDATE professor por ID

@app.route("/professores/<int:id>", methods=["PATCH"])
def update_professor(id: int):
    
    novo_nome_professor = request.get_json()

    if not novo_nome_professor or "nome" not in novo_nome_professor:
        return jsonify(error="PayLoad inválido"), 400
    
    for professor in professores:
        if professor["id"] == id:
            professor["nome"] = novo_nome_professor["nome"]
            return jsonify(msg="Nome do professor atualizado com sucesso!"), 200
        
    return jsonify(error="Professor não encontrado para atualização!"), 404



if __name__ == "__main__":
    app.run()
