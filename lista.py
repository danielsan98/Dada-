import math

lista = [24, 43, 7, 54, 3, 13, 6, 14, 5, 9, 82, 58, 30, 24]

"""for i in range(0, len(lista)):
    print(lista[i])"""

def sumaPares():
    temp=0
    for i in range(0, len(lista)):
        if lista[i]%2 == 0:
            temp+=lista[i]
    return temp

def cuadradoNones():
    listaNones=[]
    for i in range(0, len(lista)):
        if lista[i]%2 != 0:
            listaNones.append(math.pow(lista[i],2))
    return listaNones

def main():
    print(sumaPares())
    print(cuadradoNones())

if __name__ == '__main__':
    main()



    
