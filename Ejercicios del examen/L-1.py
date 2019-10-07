"""
Dibujar un triángulo de 10 renglones de alto que tenga los números primos
"""
arr = []

for i in range(0, 20):
    if i %2 != 0:
        arr.append(i)
for j in range (0,10):
    print("")
    for k in range(0,j+1):
        print(f"{arr[k]} ",end="")

print("")