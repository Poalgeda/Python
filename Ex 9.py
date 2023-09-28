#programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas


num1=int(input("Introduce un numero en segundos: "))

minutos=float(num1)/60
horas=float(num1)/3600


print("Este numero en minutos es: ", minutos, "y en horas: ", horas)

input()
