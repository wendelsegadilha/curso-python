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


for value in range(0, 50, 2):
    print(value, end=" ")

print()

#pegando os indeces de uma lista
frutas = ["Uva", "Banana", "Pêra", "Morango"]
indices = range(len(frutas))
for i in indices:
    print(i, frutas[i])


#pegando os indeces de uma lista com enumerate
for index, value in enumerate(frutas):
    print(index, value)