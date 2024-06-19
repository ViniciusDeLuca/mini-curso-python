fluxo_caixa = []

print ("1 - Adicionar despesa")
print ("Digite outro numero para encerrar")

def transacao():
    nome = input("Nome: ")
    receita = float(input("Digite o valor da receita: "))
    fluxo_caixa.append({
        "nome": nome,
        "receita": receita
    })
    return print (fluxo_caixa)
    

while True:
    opcao = int(input("Digite a opcao: "))
    
    match opcao:
        case 1:
            transacao()
