nomes = ["Wendel", "Anny", "Venes"]

nome1, nome2, nome3 = nomes

print(nome1, nome2, nome2)



frutas = ("Uva", "Morango", "Banana")

_, f2, f3 = frutas
print(f2, f3)

f1, *_ = frutas
print(f1)

_, f2, _ = frutas
print(f2)
