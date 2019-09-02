import math

a=float(input("dame a: "))
b=float(input("dame b: "))
c=float(input("dame c: "))
raiz=0

if a != 0:
    negativeB=b*-1
    d=float((math.pow(b, 2)) - (4*a*c))
    
    denominador=2*a
    if d<0:
            d=d *-1
            raiz=float(math.sqrt(d))
            print("(",negativeB, " +- ", raiz, "i", ")", " / ", 
            denominador)
    else:
            raiz=float(math.sqrt(d))
            print("(",negativeB, " +- ", raiz, "i", ")", " / ", 
            denominador)

else:
        print("a no puede ser 0!")    

  


         


    