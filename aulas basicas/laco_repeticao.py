# Laços de repetição
notas = []
for x in range(1):
    codigo_aluno = input("Matricula: ")
    nota = float(input("Nota: "))
    if nota > 10:
        nota = 10
    elif nota < 0:
        nota = 0
    else:
        nota = nota
    resultado = [codigo_aluno, int(nota)]
    notas.append(resultado)

print(notas)

contador = 1
while contador <= 3:
    codigo_aluno = input("Matricula: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, int(nota)]
    notas.append(resultado)
    # contador = contador + 1
    contador += 1