#programa que pida un número de horas y muestre por pantalla los minutos y segundos

num1=int(input("Introduce un numero en horas: "))

minutos=int(num1)*60
seg=int(num1)*3600

print("Este numero equivale a", minutos, "minutos, y a",seg, "segundos")
input()
