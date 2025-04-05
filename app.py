from flask import Flask, jsonify
from pydantic import ValidationError
from alunos.alunos_routes import alunos_blueprint
from professores.professores_routes import professores_blueprint
from turmas.turmas_routes import turmas_blueprint
from admin.admin_routes import admin_blueprint

app = Flask(__name__)

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)
app.register_blueprint(admin_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
