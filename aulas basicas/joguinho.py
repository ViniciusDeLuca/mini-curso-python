import os

player = {
    "nome": "Vinicius",
    "x": 0,
    "y": 0        
}

def andar(direcao):
    match direcao:
        case "s":
            player["x"] += 1
        case "w":
            player["x"] -= 1
        case "a":
            player["y"] -= 1
        case "d":
            player["y"] += 1
        case _:
            print("Direção inválida")

while True:
    os.system("cls")
    print(f"X: {player['x']} Y: {player['y']}")
    for x in range(5):
        print("\n")
        for y in range (10):
            if x == player["x"] and y == player["y"]:
                print("X", end="")
            else:
                print("M", end="")
    direcao = input("\nDigite a direção: ")
    andar(direcao)