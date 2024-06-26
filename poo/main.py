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
p1 = Pessoa.por_ano_nascimento(estudante.nome, estudante.idade)
print(p1.idade)