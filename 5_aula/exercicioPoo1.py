class Carro:
    modelo = ""
    marca = ""
    ano = 0
    km = 0
    cor = ""

    def __init__(self):
        print("Objeto carro criado!")
    
    def ligar(self):
        print(f"{self.modelo} ligado")
    


# Criando e manipulando objeto da classe Carro

carro1 = Carro()

carro1.modelo = "Creta"
carro1.marca = "Hyundai"
carro1.ano = 2021
carro1.cor = "branca"
carro1.km = 60000
carro1.ligar()
