# para rodar "python main.py"

# Variaveis
# nome = "Vinicius"
# idade = 22
# peso = 73

# print(nome, idade, peso)

# Inputs
# Retorna os valores como string, necessitando de conversão
# nome = input("Digite seu nome")
# idade = int(input("Digite sua idade"))
# peso = float(input("Digite seu peso"))

# Operadores
# soma = 1+1
# multiplicacao = 2*2
# divisao = 3/3
# potencia = 7**2


# Condicionais
# idade = int(input("Informe sua idade"))

# if idade >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")
    
# salario = float(input("Digite o seu salario"))

# if salario <= 3000:
#     print("Ganha baixo nengue")
# elif salario > 3000 and salario <=6000:
#     print("Programador pleno")
# elif salario > 6000 and salario <= 9000:
#     print("Programador senior")
# else:
#     print("Gerente de projetos")

# Listas
# append - adiciona um item no final
# insert - adiciona um item numa posicao especifica
# pop - remove e retorna o ultimo item
# pop (parametro posicao) - remove e retorna o item da posição
# sort - ordena a lista
# reverse - ordena ao reverso
# index (parametro item) - retorna a posição da primeira ocorrencia do item
# count (item) - retorna o número de ocorrencias do item
# remove (item) - remove a primeira ocorrencia do item

# lista_numeros = [1,2,3]

# lista_numeros.append(4)
# lista_numeros.append(5)

# print("total ", len(lista_numeros)) #tamanho
# print("menor valor ",min(lista_numeros))
# print("maior valor ",max(lista_numeros))

# Laços de repetição
notas = []
for x in range(3):
    codigo_aluno = input("Matricula: ")
    nota = float(input("Nota: "))
    if nota > 10:
        nota = 10
    elif nota < 0:
        nota = 0
    else:
        nota = nota
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print(notas)