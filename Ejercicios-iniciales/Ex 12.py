# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

alt=int(input("Introduce la altura del trapecio: "))
menor=int(input("Introduce la medida de la base menor: "))
mayor=int(input("Introduce la medida de la base mayor: "))
lado=int(input("Introduce el lado del trapecio: "))
p=int(lado)*2+int(menor)+int(mayor)
a=(float(menor)+float(mayor))*float(alt)/2
print("El perímetro es: ", p)
print("El área es: ", a)
input()
