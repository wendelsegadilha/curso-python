class Pessoa():
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf

    def get_cpf(self):
        return self.cpf
    

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    def get_cnpj(self):
        return self.cnpj
    

pf = PessoaFisica("Wendel", "123.654.789-96")
print(pf.get_nome(), pf.get_cpf())

pj = PessoaJuridica("Brasil Importados LTDA", "1458765315480001")
print(pj.get_nome(), pj.get_cnpj())