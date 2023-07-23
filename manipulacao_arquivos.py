
"""
Cria arquivo e ler
Tipos de abertura
a+
w+
r+
"""

caminho_aqruivo = "arquivos\\nomes.txt"

with open(caminho_aqruivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write("Wendel\n")
    arquivo.writelines(['Venes\n', 'Anny\n'])
    arquivo.seek(0,0) #move o cursor para o inicio
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())



