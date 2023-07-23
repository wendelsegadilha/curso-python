import os

caminho = r"C:\\Users\\Wendel"

#listando diretórios
for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(caminho_completo)

    if not os.path.isdir(pasta):
        continue
    
    for arqs in os.listdir(caminho_completo):
        print(arqs)


 