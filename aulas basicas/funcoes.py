# se declara funcao utilizando def

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    return a ** (1/2)

def raiz_cubica(a):
    return a ** (1/3)

def raiz_quarta(a):
    return a ** (1/4)

resposta = soma(1,2) + potencia(2,3) + raiz_cubica(16)

print(resposta)