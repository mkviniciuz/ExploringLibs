import random
import math

# CONCEITOS DE ALEATORIDADE CONTROLADA
# UTILIZANDO SEED E DEFININDO PATTERNS

def geradorSemente():
    seed = int(input("Seed: "))
    random.seed(seed)
    for i in range(5):
        print(random.randint(1, 100))

def terrainGenerator():
    row = 50
    column = 10
    sprites = ["^","_","~"]
    for c in range(column):
        for r in range(row):
            print(random.choice(sprites), end="")    
        print("")

def nameGenerator():
    start = ["Ka", "Lu", "Mo", "Zi", "Na", "Ta", "He"]
    middle = ["ra",  "ni", "to", "ze", "ma", "tu", "er"]
    end = ["on", "us", "el", "ar", "al", "fe", "go"]

    name = []

    name.append(random.choice(start))
    name.append(random.choice(middle))
    name.append(random.choice(end))

    print("".join(name))


def proceduralTraining():
    random.seed(input("Digite seu nome: "))

    nome = random.choice(["Ogro das Sombras", "Cavaleiro Sombrio", "Turquesa Preta", "Tramoia"])
    sufixo = random.choice(["da Tempestade", "da Sombras", "Infernal", "Cristalizado", "Sanguinario"])
    forca = random.randint(5,20)
    ataque = random.choice(["Veneno", "Fogo", "Gelo"])

    print(f"Monstro gerado: {nome} {sufixo}")
    print(f"Força: {forca}")
    print(f"Tipo de ataque: {ataque}")


def gerar_mapa():

    largura = int(input("Largura: "))
    altura = int(input("Altura: "))

    random.seed(input("Seed: "))

    blocos = [".", "#", "~", "^"]

    for alt in range(altura):
        linha = ''
        for lar in range(largura):
            linha += random.choice(blocos)
        print(linha)


    