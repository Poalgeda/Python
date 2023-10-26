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
p1=password[0]
p2=password[1]
p3=password[2]
p4=password[3]
p5=password[4]
p6=password[5]
p7=password[6]
p8=password[7]
if len(password) <=8 and len(password) >=6:
    if p1
else:
    print(f"La palabra clave tiene una longitud de {len(password)} y no cumple con los requisitos.")