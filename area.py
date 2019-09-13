import math

l1=float(input("Dame el lado 1 del triángulo: "))
l2=float(input("Dame el lado 2 del triángulo: "))
l3=float(input("Dame el lado 3 del triángulo: "))

p=float(l1+l2+l3)

s=float(p/2)

aux=float(s*((s-l1)*(s-l2)*(s-l3)))

if aux<0:
    print("Tu raiz salió negativa!")
else:
    a=float(math.sqrt(aux))
    print("El perimetro es: ", p, "\n", "El area es: ", a)
    




