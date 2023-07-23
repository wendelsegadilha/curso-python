import json

"""
Salva dados como JSON
"""
caminho_aqruivo = "arquivos\\nomes.json"
pessoa = {'nome':'Wendel','data_nascimento':'21/11/1194', 'profissão':'Programador'}

with open(caminho_aqruivo, 'w+', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

#Recupera os dados em JSON e transforma em objeto Python
with open(caminho_aqruivo, 'r', encoding='utf8') as arquivo:
    res = json.load(arquivo)
    print(res)