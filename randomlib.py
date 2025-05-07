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

def mapa_logica():

    largura = int(input("Largura: "))
    altura = int(input("Altura: "))

    random.seed(input("Seed: "))

    caminho = random.randint(1, largura-1)

    for alt in range(altura):
        linha = ''
        for lar in range(largura):
            if lar == caminho:
                linha += "."
            else:
                linha += "#"
        print(linha)

def mapa_curvo():
    
    largura = int(input("Largura: "))
    altura = int(input("Altura: "))

    random.seed(input("Seed: "))

    caminho = random.randint(0, largura-1)

    for alt in range(altura):
        linha = ''
        for lar in range(largura):
            if lar == caminho:
                linha += "."
            else:
                linha +="#"
        print(linha)


        direcao = random.choice([-1, 0 , 1])

        caminho += direcao

        caminho = max(0, min(caminho, largura-1))

def varios_caminhos():

    largura = int(input("Largura: "))
    altura = int(input("Altura: "))

    random.seed(input("Seed: "))

    def gerador_caminhos():
        quantia_caminhos = int(input("Caminhos: "))
        caminhos = []
        for i in range(quantia_caminhos):
            caminhos.append(random.randint(0, largura-1))

        return caminhos
    
    caminhos = gerador_caminhos()

    for alt in range(altura):
        linha = ''
        for lar in range(largura):
            if lar in caminhos:
                linha += "."
            else:
                linha +="#"
        print(linha)

        for i in range(len(caminhos)):
            direcao = random.choice([-1, 0 , 1])

            caminhos[i] += direcao

            caminhos[i] = max(0, min(caminhos[i], largura-1))

def gerador_senhas_sem_repeticoes(x):

    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                  '@','!','#','$','%','&','*','(',')','_','+','1','2','3','4','5','6','7','8','9','0']

    senha = random.sample(caracteres, x)

    print("".join(senha))

