#VERSIÓ 1: Realitzar un programa que permeti introduir una ‘paraula clau’ amb les següents característiques:
print("1.La contrasenya ha de tenir  entre 6 i 8 caràcters:")
print("2.Forçar els valor seguentes segons la posició indicada:")
print("     Posició 1: Major o igual a 1, o menor o igual a 5.")
print("     Posició 2: Lletra minúscula.")
print("     Posició 3: Lletra mayúscula.")
print("     Posició 4: Un dels següents símbols: *, @, _.")
print("     Posició 5: Lletra mayúscula.")
print("     Posició 6: Un número major o igual a 6 i menor o igual que 9")
print("     Posició 7: Un dels següents símbols: &, /, #.")
print("     Posició 8: Un número menor o igual a 5")
password=input("Introduce una palabra clave de entre 6 a 8 palabras: ")

if len(password) <=8 and len(password) >=6:
    print()
else:
    print(f"La palabra clave tiene una longitud de {len(password)} y no cumple con los requisitos.")

texto_error=""

pos_1=int(password[0])
if not(pos_1 >= 1 and pos_1 <= 5):
    texto_error= texto_error + "El primer digito es incorrecto, "

pos_2=password[1]
mayus=pos_2.isupper()

if not (mayus is False):
    texto_error= texto_error + "El segundo digito es incorrecto, "

pos_3=password[2]
mayus=pos_2.isupper()

if not (mayus is False):
    texto_error= texto_error + "El tercer digito es incorrecto, "

pos_4=password[3]
if not(pos_4 == "*" or pos_4 == "_" or pos_4 == "@"):
    texto_error= texto_error + "El cuarto digito es incorrecto, "

pos_5=password[4]
mayus=pos_2.isupper()

if not (mayus is False):
    texto_error= texto_error + "El quinto digito es incorrecto, "


pos_6=int(password[5])

if not(pos_6 <= 9 and pos_6 >= 6):
    texto_error= texto_error + "El sexto digito es incorrecto, "

    pos_7=password[6]

    if not(pos_7 == "&" or pos_7=="/" or pos_7 == "#"):
        texto_error= texto_error + "El septimo digito es incorrecto, "

    pos_8=int(password[7])

    if not(pos_8 <= 5):
        texto_error= texto_error + "El ocatvo digito es incorrecto, "
        texto_error= texto_error + "Error en el caracter 8."

if texto_error=="":
    print("La contraseña es valida")
else:
    print(texto_error)

input()