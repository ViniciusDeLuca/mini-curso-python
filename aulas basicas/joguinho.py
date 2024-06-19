import os

player = {
    "nome": "Vinicius",
    "x": 0,
    "y": 0        
}

def andar(direcao):
    match direcao:
        case "d":
            player["x"] += 1
        case "a":
            player["x"] -= 1
        case "w":
            player["y"] += 1
        case "s":
            player["y"] -= 1
        case _:
            print("Direção inválida")

while True:
    os.system("cls")
    print(f"X: {player['x']} Y: {player['y']}")
    for x in range(5):
        
    direcao = input("Digite a direção: ")
    andar(direcao)