"""
Existem três tipos de estruturas de dados muito utilizadas no Python, são elas:
• Listas
• Tuplas
• Conjuntos
• Dicionários
"""

letras = ["A", "E", "O"]
print(letras[0])

#insert(i, v): Insere v na posição i da lista.
letras.insert(2, "I")
print(letras)

#append(v): Insere v no fim da lista
letras.append("U")
print(letras)

#extend(nova_lista): Concatena uma lista em outra
numeros = ["1", "2", "3"]
numeros.extend(letras)
print(numeros)

#pop(i): Remove um índice específico. Quando a função pop() não tiver parâmetro o último índice será removido.
numeros.pop()
print(numeros)

#remove(v): Remove um índice duplicado da lista (no caso o valor removido será do primeiro índice duplicado)
nomes = ["Venes", "Wendel", "Rosa", "Milton", "Venes"]
nomes.remove("Venes")
print(nomes)

#count(v): Retorna o número de vezes que um valor aparece na lista.
numeros_repetidos = [1, 2, 3, 1, 8, 7, 10, 1]
qtd = numeros_repetidos.count(1)
print(qtd)

#ndex(v): Retorna o índice do valor adicionado a função.
index = letras.index("A")
print(index)

#reverse(): Inverte a ordem dos valores da lista.
consoantes = ["B", "C", "D"]
consoantes.reverse()
print(consoantes)

#sort(): Ordena a lista dentro de um padrão de comparação. Exemplo com String
consoantes.sort()
print(consoantes)


#min(lista): Retorna o menor valor da lista. Quando a lista é composta por strings o valor retornado será o do primeiro índice
#max(lista): Retorna o maior valor da lista. Quando a lista é composta por strings o valor retornado será o do último índice.
#sum(lista): Soma os valores da lista. Não serve para lista com valores que não sejam numéricos.
menor = min(numeros_repetidos)
print(menor)

maior = max(numeros_repetidos)
print(maior)

soma = sum(numeros_repetidos)
print(soma)

#len(lista): Total de elementos dentro da lista. Podemos dizer que é o peso da lista.
tamanho = len(numeros_repetidos)
print(tamanho)

#Tuplas
pessoa = ("Wendel Segadilha", "Programador", 2023, "Cristão", "venes")
print(type(pessoa), pessoa)

print(pessoa[0])
print(pessoa[-1])
print(pessoa[1:4]) #posição 1 incluída, posição 4 não inclusa

#Conjutos
conjuto = set()
print(type(conjuto))
conjuto.add(4)
print(conjuto)

#conjuntos com chaves
x = {4,5,6,9,4,8}
print(x)

#Verificando um item dentro de um conjunto
print(4 in conjuto)

#União: Une dois conjuntos em um único conjunto, caso haja duplicidade de valores esse valor não é repetido
conjunto_1 = {1,2,3}
conjunto_2 = {3,4,5,6}
uniao = conjunto_1 | conjunto_2
print(uniao)

#nterseção: Gera um novo conjunto baseado na interseção entre os dois conjuntos.
intersecao = conjunto_1 & conjunto_2
print(intersecao)

#diferença: Gera um novo conjunto baseado na diferença entre os conjuntos. Fique atento, ele não pegará a diferença entre os dois, ele verá o que o primeiro conjunto 
#da expressão possui que o segundo não possui.
diferenca = conjunto_1 - conjunto_2
print(diferenca)

#Dicionários

aluno = {"nome":"Wendel", "idade":29, "altura":1.75}
print(aluno)
print(aluno["nome"])

#pop(chave): Remove um valor específico do dicionarios através de sua chave.
aluno.pop("idade")
print(aluno)

#update({chave:valor}): Adiciona uma nova chave e valor ao dicionário
aluno.update({"nome":"Wendel Segadilha"})
print(aluno)