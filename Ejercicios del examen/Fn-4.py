def promDosListas(l1,l2):
    suma1 = 0
    suma2 = 0
    for i in l1:
        suma1 = suma1 + i
    for i in l2:
        suma2 = suma2 + i
    return suma1/len(l1)+suma2/len(l2)

def promTresListas(l1,l2,l3):
    suma1=0
    suma2=0
    suma3=0
    for i in l1:
        suma1 = suma1 + i
    for i in l2:
        suma2 = suma2 + i
    for i in l3:
        suma3 = suma3 + i
    return suma1/len(l1)+suma2/len(l2)+suma3/len(l3)
        
print(promDosListas([1,2,2,2,2,1],[2,1]))#3.1666
print(promTresListas([10,5],[6,2,2],[1]))#11.8333