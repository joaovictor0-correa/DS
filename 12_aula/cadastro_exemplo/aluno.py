class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Estudante: {self.nome} possui {self.idade} anos"