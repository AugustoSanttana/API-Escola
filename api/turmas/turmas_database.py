from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    turno = db.Column(db.String(20))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor_id'), nullable=True)