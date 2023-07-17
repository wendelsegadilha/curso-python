
"""
Fatiamento [i:f:p] [::]
OBS: o indice final não é incluso
"""
nome = "Wendel Alves Segadilha"
print(nome[2:]) # ndel Alves Segadilha
print(nome[2:6]) # ndel
print(nome[:6]) # Wendel

print(len(nome))
print(len(nome[:6])) # Wendel

#usando passo
print(nome[:23:2])

#inverter string
print(nome[::-1]) # ahlidageS sevlA ledneW