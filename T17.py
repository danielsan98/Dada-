def multiplicacion(lista):
    mult = 0
    if len(lista) > 0:
        mult = lista[0]
        for i in range(1, len(lista)):
            mult = mult * lista[i]
        return mult
    else:
        print("El arreglo no puede ser vacío!")


def main():
    lista = [5]
    print(multiplicacion(lista))

if __name__ == '__main__':
    main()

