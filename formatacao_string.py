
"""
FORMATAÇÃO DE TEXTOS
"""
#f-string
nome = "Wendel Segadilha"
profissao = "Programador"
salario = 2500
mensgem = f"O meu nome é {nome} e minha profissão é {profissao}, meu salário é de {salario:.2f}"
print(mensgem)

#metódo format()
mensgem_formatado = "O meu nome é {0} e minha profissão é {1}, meu salário é de {2:.2f}".format(nome, profissao, salario)