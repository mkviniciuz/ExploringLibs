    start = ["Ka", "Lu", "Mo", "Zi", "Na", "Ta", "He"]
    middle = ["ra",  "ni", "to", "ze", "ma", "tu", "er"]
    end = ["on", "us", "el", "ar", "al", "fe", "go"]

    name = []

    name.append(random.choice(start))
    name.append(random.choice(middle))
    name.append(random.choice(end))

    print("".join(name))