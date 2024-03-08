var=input("")
lista=var.split()
if int(lista[0]) > int(lista[1]) and int(lista[0]) > int(lista[2]):
    print(lista[0])
elif int(lista[1]) > int(lista[0]) and int(lista[1]) > int(lista[2]):
    print(lista[1])
elif int(lista[2]) > int(lista[0]) and int(lista[2]) > int(lista[1]):
    print(lista[2])
elif lista[0]==lista[1] and lista[0]==lista[2]:
    print(lista[0])
elif lista[0]==lista[1]:
    print(lista[0])