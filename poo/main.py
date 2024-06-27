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
ano_nascimento = estudante.ano_atual - int(estudante.idade)
p1 = estudante.por_ano_nascimento(estudante.nome, ano_nascimento, estudante.peso, estudante.curso)
print(p1.gera_id())