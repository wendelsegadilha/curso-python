
#https://docs.python.org/3/library/exceptions.html
def dividir(var1, var2):
    try:
        return var1 / var2
    except Exception as e:
        print("Erro: %s" %str(e))

result = dividir(10, 0)
print(result)

    
