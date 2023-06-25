msg = 'Wendel'
print(msg)

idade = 29
print(type(idade))

salario = 2500.99
print(type(salario))

casado = True
print(type(casado))

nome = "Wendel Segadilha"
print(type(nome))

profissao = "Programador"

"""
ja essa lista com os símbolos completos
• %s: string;
• %d: inteiro;
• %o: octal;
• %x: hexadecimal;
• %f: real;
• %e: real exponencial;
• %%: sinal de percentagem.
"""

print("Meu nome é " + nome + ", e sou " + profissao)

print("Meu nome é %s e sou %s." %(nome, profissao))

#vetores
estados = ["MA", "SP", "ES", "BH"]
print(estados[0])
print(estados[1])
print(estados[2])
print(estados[3])

print(1 + 3)
print(1 - 3)
print(1 * 3)
print(10 / 2)
print(10**2)
print(10 // 3)
print(10 % 3)

print(not 5 > 4)

print(not 5 == 4)

print(5 == 5 and 6 == 6)
print(5 == 4 or 6 == 6)


if idade > 30:
    print('meia de idade')
elif idade > 18:
    print("maior de idade")
else:
    print("menor de idade")