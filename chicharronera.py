import math

def chicharron():
    a=(float)input('Dame a')
    b=(float)input('Dame b')
    c=(float)input('Dame c')

    if a>0 || a<0:
        negativeB=b*-1
        d=(float)(math.pow(b, 2)) - (4*a*c)
        raiz=(float)math.sqrt(d)
        denominador=2*a
        if raiz<0:
            raiz=raiz *-1
            print('(',negativeB, ' +- ' raiz, 'i', ')', ' / ', 
            denominador)
        else:
            print('(',negativeB, ' +- ' raiz, ')', ' / ', 
            denominador)
    else:
        print('a no puede ser 0!')        
         


    