#Importa da Classe conta o método construtor Conta()
from Conta import Conta

# Cria objeto c que representa a Conta
c = Conta()

#Exibe o valor inicial do número e saldo da conta
print(f"Conta: {c.numero} possui saldo de {c.saldo}")

c.numero = "12345-6"
c.saldo = 100.0


print(f"Conta: {c.numero} possui saldo de {c.saldo}")