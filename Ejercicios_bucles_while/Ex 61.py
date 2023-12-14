#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40. 

resultado=0
var1=int(input("Introduze el numero para multiplicar: "))
multiplicador=1
tabla=False
while resultado < 40:
    if multiplicador != 11:
        resultado=var1*multiplicador
        multiplicador += 1
        print(resultado)
    else:
        print("Fin de programa.")
        break