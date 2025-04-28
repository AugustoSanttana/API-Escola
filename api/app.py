from flask_sqlalchemy import SQLAlchemy

from alunos.alunos_routes import alunos_blueprint
from professores.professores_routes import professores_blueprint
from turmas.turmas_routes import turmas_blueprint
from admin.admin_routes import admin_blueprint
from config import app

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)
app.register_blueprint(admin_blueprint)

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
    
