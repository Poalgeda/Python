var=input("")
lista=var.split()
if len(lista) == 2:
    print(int(lista[0])+int(lista[1]))
else:
    var1=input("")
    lista+=var1.split()
    print(int(lista[0])+int(lista[1]))