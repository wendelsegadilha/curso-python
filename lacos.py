cont = 0

while (cont < 10):
    print(cont)
    cont += 1

    estados = ["MA", "SP", "RJ", "ES", "AM"]

    for e in estados:
        print(e)

print("=================")

for i in range(0, len(estados)):
    if estados[i] == "RJ":
        estados[i] = "DF"

print(estados)