lista = [
    'wendel', 1.1, 2, True, [0,1,2,3], (1,2),{0,1}, {'nome':'Wendel', 'idade': 28},
]

for item in lista:
    if isinstance(item, set):
        print('SET',item)

    if isinstance(item, str):
        print('STR',item)

    if isinstance(item, int):
        print('INT',item)

    if isinstance(item, float):
        print('FLOAT', item)
    
    if isinstance(item, bool):
        print('BOOL', item)

    if isinstance(item, tuple):
        print('TUPLE', item)
    
    if isinstance(item, list):
        print('LIST', item)