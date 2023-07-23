class Contato:
    def __init__(self):
        self.celular = None
        self.email = None

class Cliente:
    def __init__(self, nome):
        self._nome = nome
        self._contato = Contato()

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def contato(self):
        return self._contato
    
    def definir_contato(self, celular, email):
        self._contato.celular = celular
        self._contato.email = email
    
    @classmethod
    def cria_cliente(cls, nome):
        return cls(nome)
    

c1 = Cliente("Wendel")
c1.definir_contato('(98)98600-3186','wendelsegadilha99@gmail.com')
print(c1.nome)
print(c1.contato.email)
print(c1.contato.celular)

c2 = Cliente.cria_cliente("Venes")
print(c2.nome)