var=input("")
lista=var.split()
if len(lista) == 3:
    print(int(lista[0])+int(lista[1])+int(lista[2]))
elif len(lista) == 2:
    var1=input("")
    lista+=var1.split()
    print(int(lista[0])+int(lista[1])+int(lista[3]))
elif len(lista) == 1:
    var1=input("")
    lista+=var1.split()
    if len(lista) == 2:
        var1=input("")
        lista+=var1.split()
        print(int(lista[0])+int(lista[1])+int(lista[2]))
    else:
        print(int(lista[0])+int(lista[1])+int(lista[2]))