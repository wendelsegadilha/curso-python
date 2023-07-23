import os


caminho = os.path.join('pasta01', 'pasta02', 'teste.txt')
print(os.path.exists(caminho))

print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)
