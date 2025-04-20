import random
import noise


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


    