
try:
    resultado = 10 / 0
    print(resultado)
except:
    print("Não pode dividir por zero")

try:
    print(int('a'))
except:
    print("Não é um número")
