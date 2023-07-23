import json


class Pessoa:

    qtd_pessoa = 0

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        Pessoa.qtd_pessoa+=1

    def get_nome_completo(self):
        print(f'{self.nome} {self.sobrenome}'.upper())

p1 = Pessoa('Wendel', 'Segadilha')
p2 = Pessoa('Venes', 'Lopes')

p1.get_nome_completo()
p2.get_nome_completo()

print(p1.__dict__)

print(f'Pessoas criadas = {Pessoa.qtd_pessoa}')

p1_json = 'programacao_orientada_objetos\\p1.json'
with open(p1_json, 'w+', encoding='utf8') as p:
    json.dump(p1.__dict__, p)