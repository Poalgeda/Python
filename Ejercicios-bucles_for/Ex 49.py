#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra=input("Introduce una palabra: ")

for cont in range(0, len(palabra)):
    letra=input("Introduce una letra: ")
    pos_letra=palabra.find(letra) + 1
    if letra in palabra and len(letra)==1:
        print(f"La letra {letra} existe y se encuantra en la posición {pos_letra}.")
    else:
        print(f"La letra {letra} no existe.")