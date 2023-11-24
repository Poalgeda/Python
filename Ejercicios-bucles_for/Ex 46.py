#A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

var1=input("Introduce una palabra: ")
vocales="aeiouáéíóúàèìòùAEIOUÀÈÌÒÙÁÉÍÓÚ"
consonantes="bcçdfghjklmnñpqrstvwxyzBCÇDFGHJKLMNÑPQRSTVWXYZ"
total_voc= ""
total_con= ""
for var_rec in var1:
    if var_rec in vocales:
        total_voc += var_rec
    elif var_rec in consonantes:
        total_con += var_rec

print(f"Las vocales de la palabra{var1} son: {total_voc}")
print(f"Las consonantes de la palabra{var1} son: {total_con}")
input()