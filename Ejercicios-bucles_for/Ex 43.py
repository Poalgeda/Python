#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra

palabra=input("Introduce una palabra: ")
posicion=0

for var_recorrer in palabra:
    print(f"En la posicion {posicion} esta la letra {var_recorrer}")
    posicion = posicion+1