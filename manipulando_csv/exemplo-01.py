import csv
"""
lendo CSV
"""
caminho = "manipulando_csv\\usuarios.csv"

"""
with open(caminho, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
"""

with open(caminho, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)