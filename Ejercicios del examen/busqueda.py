import random

def buscar(lista,num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
    return -1

lista = [random.randint(0,100) for _ in range(10000)]
print(buscar(lista,7))
print(buscar(lista,99))
print(buscar(lista,101))
print(buscar(lista,44))