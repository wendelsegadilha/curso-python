import pprint

def p(v):
    pprint.pprint(v)

#print(list(range(0,10)))

#List comprehension em Python (filtro)
lista_nova = [numero for numero in range(10) if (numero % 2) == 0]
print(lista_nova)


produtos = [
    {'nome':'Notebook', 'valor':2500},
    {'nome':'Placa de vídeo', 'valor':1300},
]

#mapeamento
novos_produtos = [
    {**produto, 'valor': produto['valor'] * 1.05}
    for produto in produtos
]

p(novos_produtos)