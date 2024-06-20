# Condicionais
idade = int(input("Informe sua idade"))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    
salario = float(input("Digite o seu salario"))

if salario <= 3000:
    print("Ganha baixo nengue")
elif salario > 3000 and salario <=6000:
    print("Programador pleno")
elif salario > 6000 and salario <= 9000:
    print("Programador senior")
else:
    print("Gerente de projetos")
