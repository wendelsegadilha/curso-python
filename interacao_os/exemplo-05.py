import os

caminho = r"C:\\Users\\Wendel\\Downloads"

#listando diretórios de forma recursiva
for root, dirs, files in os.walk(caminho):
    print(root)
    for d in dirs:
        print('  ', d)

    for f in files:
        print( '    ', f)


 