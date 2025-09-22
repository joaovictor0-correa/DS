# Criação de lista "rioPardoOne" com nomes de empresas como valores
rioPardoOne = ["Tech Aplicativos", "Tech4Pet", 
"Clínica Dente Brilhante", "Clínica de Fisioterapia Endireite-se", 
"Escola de Idiomas BIT"]

# imprime na tela a lista com todos os valores (nomes de empresas)
print(rioPardoOne)

# imprime o valor armazenado na posição da lista especificada entre "[ ]"
print(rioPardoOne[3])

#Laço for que permite a iteração sobre uma lista
# Onde "empresa" é a variável que armazena o valor encontrado
# sequencialmente na lista rioPardoOne e o imprime na tela
# um de cada vez. 
for empresa in rioPardoOne:
    print(f"Empresa: {empresa}")

print("********** Fim da Listagem ***************")
# Adiciona um novo elemento ao final da lista 
rioPardoOne.append("Café Bom Exportações")

# Executando novamente o for para percorrer a lista e exibir 
# os nomes das empresas, incluindo a recém adicionada.
for empresa in rioPardoOne:
    print(f"Empresa: {empresa}")
print("********** Fim da Listagem ***************")

# Removendo a empresa ou elemento "Clínica de Fisioterapia Endireite-se"
rioPardoOne.remove("Clínica de Fisioterapia Endireite-se")

# Executando novamente o for para percorrer a lista e exibir 
# os nomes das empresas atualizados.
for empresa in rioPardoOne:
    print(f"Empresa: {empresa}")

print("********** Fim da Listagem ***************")

