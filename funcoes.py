def somar():
    valor1 = 1
    valor2 = 2
    print(valor1 + valor2)

somar()

def subtrair(var1, var2):
    print(var1-var2)

subtrair(10,5)


def dividir(var1, var2 = 1):
    print(var1 / var2)

dividir(10)

dividir(var2=5, var1=1)

#funções com parâmetros especiais

#args é interpretado como uma tupla
def soma_tudo(var, *args):
    print(var, args)

soma_tudo(33, 10, 20, 30)

def imprime(var, **kwargs):
    print(var)
    print(kwargs)

#kwargs é interpretado como um dicionário
imprime(28, nome="Wendel", profissao="programador", sexo="Masculino")


def somar_retorno(var1, var2):
    return (var1+var2)

resultado = somar_retorno(10, 10)
print("Resultado é %d" %resultado)


