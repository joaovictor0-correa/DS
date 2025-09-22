class Conta:
    numero = "00000"
    saldo = 0.0

    def __init__ (self):
        print("Criando o objeto!")
    
    def depositar(self,valor):
        self.saldo = self.saldo + valor


#Fim da classe Conta

# Cria objetos c1,c2,c3 que representam contas distintas
c1 = Conta()
c2 = Conta()
c3 = Conta()

#Exibe o valor inicial do número e saldo da conta c
print(f"Conta1 indefinida: {c1.numero} possui saldo inicial de {c1.saldo}")

c1.numero = "12345-6"
c1.saldo = 100.0

print(f"Conta1: {c1.numero} possui saldo de {c1.saldo}")

c1.depositar(200)
print(f"Conta1: {c1.numero} saldo atualizado: {c1.saldo}")

#Exibe o valor inicial do número e saldo da conta c2
print(f"Conta2 indefinida: {c2.numero} possui saldo inicial de {c2.saldo}")

c2.numero = "9999-9"
c2.saldo = 1500.0

print(f"Conta2: {c2.numero} possui saldo de {c2.saldo}")


#Exibe o valor inicial do número e saldo da conta c3
print(f"Conta3 indefinida: {c3.numero} possui saldo inicial de {c3.saldo}")

c3.numero = "567898-0"
c3.saldo = 300.0

print(f"Conta3: {c3.numero} possui saldo de {c3.saldo}")