#Ejercicio 4
s95=1.765
s98=1.913
ga=1.746
ga2=1.839
print("****GASOLINERA****")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
print("******************")
gasolina=int(input("Escoja el tipo de combustible: "))
if gasolina==1:
    lit=float(input("Introduzca el número de litros a repostar: "))
    precio=lit*s95
    print("El precio a pagar es: ",precio)
elif gasolina==2:
    lit=float(input("Introduzca el número de litros a repostar: "))
    precio=lit*s98
    precio2=precio/100*90
    print("El precio a pagar es: ",precio,"y con el descuento queda en: ", precio2)
elif gasolina==3:
    lit=float(input("Introduzca el número de litros a repostar: "))
    precio=lit*ga
    print("El precio a pagar es: ",precio)
elif gasolina==4:
    lit=float(input("Introduzca el número de litros a repostar: "))
    precio=lit*ga2
    precio2=round(precio/100*88, 2)
    print("El precio a pagar es: ",precio,"y con el descuento queda en: ", precio2)
else:
    print("El valor introducido no esta dentro del menú de selección")