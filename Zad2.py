from random import randint

lista1 = []

for i in range(10):
    liczba = randint(0, 99)
    lista1.append(liczba)

print(lista1)

lista2=[j for j in lista1 if j % 2 == 0]