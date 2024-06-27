from pessoa import Pessoa
from random import randint
class Estudante(Pessoa):
    def __init__(self, nome, idade, peso, curso, aprovado=False):
        super().__init__(nome, idade, peso)
        self.curso = curso
        self.aprovado = aprovado
    
    def __str__(self):
        return f"Estudante(nome={self.nome}, idade={self.idade}, peso={self.peso}, curso={self.curso}, aprovado={self.aprovado})"
    
    def getCurso(self):
        return self.curso
    
    def apresentar(self):
        return super().apresentar()
    
    def aprovar(self):
        if not self.aprovado:
            self.aprovado = True
        return
        
    def reprovar(self):
        if self.aprovado:
            self.aprovado = False
        return
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento, peso, curso):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade, peso, curso)
    
    @staticmethod
    def gera_id():
        random = randint(1, 10000)
        return random