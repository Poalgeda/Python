#Realiza el ejercicio del DNI que encontrarás en el Sway
respuesta="s"
lista_intentos=[]
nif=[]
nif_mal=[]
nifs_total=0
errores=0
menu="s"
while respuesta=="s":
    correccion=False
    while correccion==False:
        num_dni=input("Introduce el numero del DNI (8 caracteres): ")
        if len(str(num_dni)) !=8:
            print("El valor introducido no cumple con la longitud correcta.")
            lista_intentos+="0".split(",")
            nif_mal+=num_dni.split(",")
            errores+=1
        elif not num_dni.isnumeric():
            print("El valor no es numerico.")
            lista_intentos+="1".split(",")
            nif_mal+=num_dni.split(",")
            errores+=1
        else:
            correccion=True
            lista_intentos+="3".split(",")

    resto_letra=int(num_dni)%23
    if resto_letra <= 22:
        if resto_letra == 0 :
            letra="T"
        elif resto_letra == 1 :
            letra="R"
        elif resto_letra == 2 :
            letra="W"
        elif resto_letra == 3 :
            letra="A"
        elif resto_letra == 4 :
            letra="G"
        elif resto_letra == 5 :
            letra="M"
        elif resto_letra == 6 :
            letra="Y"
        elif resto_letra == 7 :
            letra="F"
        elif resto_letra == 8 :
            letra="P"
        elif resto_letra == 9 :
            letra="D"
        elif resto_letra == 10 :
            letra="X"
        elif resto_letra == 11 :
            letra="B"
        elif resto_letra == 12 :
            letra="N"
        elif resto_letra == 13 :
            letra="J"
        elif resto_letra == 14 :
            letra="Z"
        elif resto_letra == 15 :
            letra="S"
        elif resto_letra == 16 :
            letra="Q"
        elif resto_letra == 17 :
            letra="V"
        elif resto_letra == 18 :
            letra="H"
        elif resto_letra == 19 :
            letra="L"
        elif resto_letra == 20 :
            letra="C"
        elif resto_letra == 21 :
            letra="K"
        elif resto_letra == 22 :
            letra="E"

        dni=str(num_dni)+"-"+letra
        nif+=dni.split(",")
        nifs_total+=1
        print(dni)
    else:
        #si el resto es incorrecto:
        print("Error")
        lista_intentos+="2".split(",")
        errores+=1
    respuesta=input("Quieres hacer otro calculo? s/n ")

while menu=="s":
    print("**************RESULTADOS**************")
    print("1.Listar NIF correcto de menor a mayor.")
    print("2.Listar DNI incorrecto de menor a mayor.")
    print("3.Numero total de errores producidos.")
    print("4.Numero total de DNI correctos.")
    print("5.Porcentages lista_intentos con error y sin error.")
    print("6.Salir")
    var1=input("Elige una opcion: ")
    #Los distintos prints con guiones son para crear un poco mas de espacio para que el usuario vea bien.
    if var1=="1":
        print("---------------------")
        nif.sort()
        print(nif)
        print("---------------------")
    elif var1=="2":
        print("---------------------")
        nif_mal.sort()
        print(nif_mal)
        print("---------------------")
    elif var1== "3":
        print("---------------------")
        print(errores)
        print("---------------------")
    elif var1 == "4":
        print("---------------------")
        print(nifs_total)
        print("---------------------")
    elif var1 == "5":
        print("---------------------")
        print(f"El numero de intentos es: {round(len(lista_intentos), 1)}")
        correcto=lista_intentos.count("3")
        print(f"El porcentage de DNI correctos es {round(correcto/len(lista_intentos)*100, 1)} %")
        incorrecto=lista_intentos.count("0")+lista_intentos.count("1")+lista_intentos.count("2")
        print(f"El porcentage de DNI correctos es {round(incorrecto/len(lista_intentos)*100, 1)} %")
        incorrecto_longitud=lista_intentos.count("0")
        print(f"El porcentage de DNI correctos es {round(incorrecto_longitud/len(lista_intentos)*100, 1)} %")
        incorrecto_digitos=lista_intentos.count("1")
        print(f"El porcentage de DNI correctos es {round(incorrecto_digitos/len(lista_intentos)*100, 1)} %")
        incorrecto_resto=lista_intentos.count("2")
        print(f"El porcentage de DNI correctos es {round(incorrecto_resto/len(lista_intentos)*100, 1)} %")
        print("---------------------")
    elif var1=="6":
        print("---------------------")
        print("Fin del programa")
        print("---------------------")
        menu="n"