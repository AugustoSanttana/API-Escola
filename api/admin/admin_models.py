from database import banco_de_dados

alunos: list = banco_de_dados['alunos']
professores: list = banco_de_dados['professores']
turmas: list = banco_de_dados['turmas']

class ModelAdmin():
    def __init__(self) -> None:
        ...
    
    def resetar(self):
        alunos.clear()
        professores.clear()
        turmas.clear()
        