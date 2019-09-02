import math

a=float(input("dame a: "))
b=float(input("dame b: "))
c=float(input("dame c: "))
raiz=0

if a != 0:
    negativeB=b*-1
    d=((math.pow(b, 2)) - (4*a*c))
    raiz=float(math.sqrt(d))
    denominador=2*a
    if raiz<0:
            raiz=raiz *-1
            print("(",negativeB, " +- ", raiz, "i", ")", " / ", 
            denominador)
    else:
            print("(",negativeB, " +- ", raiz, "i", ")", " / ", 
            denominador)
else:
        print('a no puede ser 0!')    


         


    