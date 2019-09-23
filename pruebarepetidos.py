
"""
for i in range(0, len(arr)):
    print(arr[i])
    """
"""
for arr in arrNew:
    arr.append(arr.remove())
    
print(arr)
"""
def fan():
    arr=[9, 3 ,1, 3, 2, 9]
    arrNew=[]
    for j in range(0, len(arr)):
        aux=False
        for k in range(j, len(arr)):
            if k != j:
                if arr[j] == arr[k]:
                   aux=True
        if aux==False:
            arrNew.append(arr[j])
        for i in range(0, len(arrNew)):
            if arrNew[i] == arr[i]:
                arrNew.remove(arrNew[i])
        for i in range(0,len(arrNew)):
            if arrNew[i] == arr[k]:
                arrNew.remove(arrNew[i])
            
    return arrNew

            


        

def eliminar():
    arr=[9, 3 ,1, 3, 9, 2]
    arrNew=[]
    temp=0
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if temp==arr[i]:
                arr.remove(arr[i])
                if  arr[i] == arr[j]:
                   arr.remove(arr[i])
                   #arrNew.append(arr[j])
                   temp=arr[i]
    return arr


def accion(arreglo):
    arrNew=[]
    for i in range(0, len(arreglo)):
        if i not in arreglo:
            arrNew.append(i)
    return arrNew



def remover(arreglo):
    arrNew=[]
    for i in arreglo:
        if i not in arrNew:
         arrNew.append(i)
    return arrNew

def main():
    
    arr=[9, 3 ,1, 3, 9, 2]
    """
    print("Lista original: ", arr)
    arr=list(set(arr))
    print("Nueva lista con elementos unicos: ", arr)
    #arr=remover(arr)"""

    #print(remover(arr))
    print(fan())
    #print(eliminar())

if __name__ == '__main__':
    main()


"""
for i in range(0, len(arr)):
    for j in range(1, len(arr)-1):
        if  arr[i] == arr[j]:
            #arr.remove(arr[i])
            arrNew.append(arr[j])"""



            


        