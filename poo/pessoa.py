from datetime import datetime
class Pessoa(object):
    ano_atual = int(datetime.now().year)
    
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade}, peso={self.peso})"
        
        
    def getNome(self):
        return self.nome
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = int(cls.ano_atual) - int(ano_nascimento)
        return cls(nome, idade)