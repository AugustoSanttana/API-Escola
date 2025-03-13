from flask import Flask, jsonify, request
from database import banco_de_dados

app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def get_alunos():
  return jsonify(banco_de_dados["alunos"])

if __name__ == "__main__":
  app.run(debug=True)