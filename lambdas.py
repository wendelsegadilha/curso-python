pessoas = [
    {'nome':'Wendel', 'idade':28},
    {'nome':'Venes', 'idade':29},
    {'nome':'Anny', 'idade':9},
]
"""
def orederna(item):
    return item['nome']
"""
#usando lambda
pessoas.sort(key=lambda item:item['idade'], reverse=True)

print(pessoas)