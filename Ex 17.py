#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

peso=int(input("Introduce tu peso en kg: " ))
alt=float(input("Introduce tu altura en metros: "))
imc=peso/(alt**2)
imcr= round (imc, 2)
if imc >= 25:
    print("Si pesas", float(peso) ,"y mides", float(alt),"tienes un IMC de", imcr,". Hay sobrepeso.")
else:
    print("Si pesas", float(peso) ,"y mides", float(alt),"tienes un IMC de.", imcr)


input ()
