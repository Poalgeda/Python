#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes: 

var1=input("Introduce una palabra: ")
vocales="aeiouáéíóúàèìòù"
consonantes="bcdfghjklmnpqrstvwxyz"
total_voc= ""
total_con= ""
for var_rec in var1:
    if var_rec in vocales:
        total_voc += var_rec
    else:
        total_con += var_rec

print(f"Las vocales de la palabra{var1} son: {total_voc}")
print(f"Las consonantes de la palabra{var1} son: {total_con}")
input()
