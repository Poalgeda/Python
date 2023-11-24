#Realiza un programa donde el usuario introduzca números y el programa indique si es par o impar. El programa finaliza cundo el usuario introduzca "-99".


var=int(input("Introduce un numero: "))
while var != -99:
    if var%2==0:
        print("el numero es par")
    if var%2==1:
        print("el numero es impar")
        var=int(input("Introduce un numero: "))
else:
    print("programa finalizado")