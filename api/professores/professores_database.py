from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nulable=True)
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.String(20))
    disciplina = db.Column(db.String(20))
    salario = db.Column(db.Float)
    