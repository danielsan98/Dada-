
arreglo=[9,12,3,0,1,4] 
arrAux=[]
aux=0
num = int(input("Entre que numero quieres saber si son divisibles?: "))
for i in range(len(arreglo)):
    if((arreglo[i]%num)==0):
        if(arreglo[i]!=0):
            arrAux.append(arreglo[i])
            aux=aux+1
if(range(len(arrAux))==0):
    print("No hay ningun valor divisible entre ", num)
else:
    print(arrAux)
        
