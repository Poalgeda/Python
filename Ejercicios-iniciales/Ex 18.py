#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
precio_adultos=12/100*90
precio_menores=12/100*50
adultos=int(input("Introduce el numero de adultos que accederán: "))
menores=int(input("Introduce el numero de menores que accederán: "))
tot_adultos=round(precio_adultos*adultos, 1)
tot_menores=round(precio_menores*menores, 1)

print("El precio total para 1 menor/es es: ",float(tot_menores))
print("El precio total para 1 adulto/s es: ",float(tot_adultos))
input()
