class Forma:
    def __init__(self,nome):
        self.nome = nome

    def calculaArea(self):
        raise NotImplementedError("O método deve ser implementado em subclasse")

    def calculaPerimetro(self):
        raise NotImplementedError("O método deve ser implementado em subclasse")

    def __str__(self):
        return f"Nome da forma geométrica: {self.nome}"