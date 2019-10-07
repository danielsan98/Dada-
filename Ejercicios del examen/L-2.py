''' L-2
Dibujar piramide de *'''

altura = 5
espacio = altura - 1
contador = 1

for x in range(altura):
    while espacio >=0:
        print ('%s%s%s'%((' '*espacio), ('*'*contador),(' '*espacio)))
        espacio -=1
        contador +=2
