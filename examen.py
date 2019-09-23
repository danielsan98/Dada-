def dejarUnicos(arreglo):
    arrNew=[]
    for i in arreglo:
        if i not in arrNew:
         arrNew.append(i)
    return arrNew

def removerTodosRepetidos():
    arr=[9, 3 ,1, 3, 2, 9]
    arrN=[]
    for j in range(0, len(arr)):
        aux=False
        for k in range(j, len(arr)):
            if k != j:
                if arr[j] == arr[k]:
                   aux=True
        if aux==False:
            arrN.append(arr[j])
        for i in range(0, len(arrN)):
            if arrN[i] == arr[i]:
                arrN.remove(arrN[i])
        for i in range(0,len(arrN)):
            if arrN[i] == arr[k]:
                arrN.remove(arrN[i])
            
    return arrN

def main():
    arr=[9, 3 ,1, 3, 9, 2]
    print("El arreglo original es: ", arr)
    print("Eliminando repetidos y dejando solo uno de ellos: ", dejarUnicos(arr))
    print("Eliminando solamente repetidos: ", removerTodosRepetidos())


if __name__ == '__main__':
    main()