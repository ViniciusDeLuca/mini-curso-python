import re

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto (self, percentual):
        self.preco = self.preco - ((self.preco * percentual) / 100)
        
    # Getter
    
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco (self, valor):
        if isinstance(valor, str):
            valor = re.sub(r'[^\d,]', '', valor)
            valor = valor.replace(',', '.')
            valor = float(valor)
        self._preco = valor
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        valor = valor.title()
        self._nome = valor
        return self._nome
     
produto1 = Produto(
    nome="camiseta",
    preco = int(50)
)
produto2 = Produto(
    nome="calça",
    preco = 'R$90'
)

produto2.desconto(15)
print(produto2.nome)