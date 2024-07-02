class BaseDeDados:
    def __init__(self):
        self.dados = {}
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})
        
bd = BaseDeDados()