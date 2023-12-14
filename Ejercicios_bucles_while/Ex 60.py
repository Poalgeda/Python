#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while 
resultado=0
var1=int(input("Introduze el numero para multiplicar: "))
multiplicador=1
tabla=False
while tabla==False:
    if multiplicador != 11:
        resultado=var1*multiplicador
        multiplicador += 1
        print(resultado)
    else:
        tabla=True
        print("Fin del programa")

