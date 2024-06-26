from pessoa import Pessoa
from estudante import Estudante

pessoa = Pessoa(
    nome="Vinicius",
    idade=22,
    peso=73
)

estudante = Estudante(
    nome="Vinicius",
    idade= 23,
    peso= 73,
    curso="POO"
)

estudante.aprovar()
print(estudante.aprovado)