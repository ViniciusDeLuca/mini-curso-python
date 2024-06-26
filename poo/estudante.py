from pessoa import Pessoa
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