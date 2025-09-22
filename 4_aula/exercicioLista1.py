""" Criar uma lista em Python com nomes de times da Série A do 
Campeonato de Futebol Paulista. 
Comece a lista com o seu time e peça para o 
usuário cadastrar outros 3 times. 
Escolha um time para remover...
A cada operação, exiba a lista de times atualizada!
 """

times = ["Corinthians"]

for time in times:
    print(time) 

timeAdicional1 = input("Digite mais um nome de time para adicionar:")
if timeAdicional1 in times:
    print("Time já cadastrado!")
else:    
    times.append(timeAdicional1)
print("Lista atualizada:")
for time in times:
    print(time)
print("**************************")

timeAdicional2 = input("Digite mais um nome de time para adicionar:")
if timeAdicional2 in times:
    print("Time já cadastrado!")
else:    
    times.append(timeAdicional2)

print("Lista atualizada:")
for time in times:
    print(time)
print("**************************")

timeAdicional3 = input("Digite mais um nome de time para adicionar:")
if timeAdicional3 in times:
    print("Time já cadastrado!")
else:    
    times.append(timeAdicional3)

print("Lista atualizada:")
for time in times:
    print(time)
print("**************************")

escolha = input("Escolha um time para ser removida da lista:")

times.remove(escolha)

print("Lista atualizada:")
for time in times:
    print(time)
print("**************************")

