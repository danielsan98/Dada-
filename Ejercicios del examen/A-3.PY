'''
Dado un arrgeglo, contar numeros positivos y sumar negativos 
'''

def positivosNegativos(arr):
    positivos = 0
    negativos = 0

    for i in range(0,len(arr)):
        if arr[i] < 0:
            negativos += arr[i]
        elif arr[i] > 0:
            positivos +=1
            
    print(positivos," positivos, ",negativos," la suma de los negativos")

datos = [1,2,3,4,5,6,-11,-12,-13,-14,-15,0]

positivosNegativos(datos)