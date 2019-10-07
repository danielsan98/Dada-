"""
Pintar los números primos y no primos del 2 al 100
"""

def obtenerNumeros(n):
    primos = [True for i in range (n+1)]
    
    for i in range(2,n+1):
        numDos=2
        while i*numDos <= n:
            primos[i*numDos] = False
            numDos += 1
    print("Primos: ")
    for i in range (2,n+1):
        if primos[i] == True:
            print(f"{i}, ",end='')
    print("\n\nNo primos: ")
    for i in range (2,n+1):
        if primos[i] == False:
            print(f"{i}, ",end='')


obtenerNumeros(100)
print("")