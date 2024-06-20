class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade}, peso={self.peso})"
        
        
    def getNome(self):
        return self.nome