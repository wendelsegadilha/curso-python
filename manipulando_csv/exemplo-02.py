"""
Salvando CSV
"""

import csv

caminho_csv = "manipulando_csv\\clientes.csv"

lista_clientes = [
    {"nome":"Wendel", "credito":1500.98},
    {"nome":"Venes", "credito":2890.47},
]

#print(lista_clientes[0].keys())

with open(caminho_csv, 'w', encoding='utf8') as arquivo:

    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)
    escritor.writerow(nome_colunas)

    for clinte in lista_clientes:
        escritor.writerow(clinte.values())
    