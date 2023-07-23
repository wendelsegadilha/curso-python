"""
Salvando CSV
"""

import csv

caminho_csv = "manipulando_csv\\clientes_liesta.csv"

lista_clientes = [
    ["Wendel", 1500.98],
    ["Venes", 2890.47]
]

with open(caminho_csv, 'w', encoding='utf8') as arquivo:

    nome_colunas = ["Nome", "Crédito"]
    escritor = csv.writer(arquivo)
    escritor.writerow(nome_colunas)

    for clinte in lista_clientes:
        escritor.writerow(clinte)
    