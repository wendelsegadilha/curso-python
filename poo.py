#https://docs.python.org/pt-br/3/tutorial/classes.html

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    #Encapsulamento (get)
    @property
    def idade(self):
        self.__idade

    #Encapsulamento (set)
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def saudar(self):
        print("Olá %s %s seja bem vido! Você tem %d anos de idade" %(self.nome, self.sobrenome, self.__idade))

wendel = Pessoa('Wendel', 'Segadilha')
wendel.idade = 28
wendel.saudar()