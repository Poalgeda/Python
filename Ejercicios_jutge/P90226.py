var=input("")

lista_original=var.split(" ")
lista_sort=var.split(" ")
if lista_original[0] == lista_original[1]:
    print(lista_original[0],"=",lista_original[1])
else:
    lista_sort.sort()
    i=lista_original.index(lista_sort[0])

    if i==0:
        print(lista_original[0],"<",lista_original[1])
    elif i==1:
            print(lista_original[0],">",lista_original[1])
            