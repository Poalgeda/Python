# Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el  usuario tenga x oportunidades para ver si letra introducida está en esa palabra.ç
palabra=input("Introduce una palabra: ")

for cont in range(0, len(palabra)):
    letra=input("Introduce una letra: ")
    if letra in palabra and len(letra)==1:
        print(f"La letra {letra} existe.")
    elif:
        print(f"La letra {letra} no existe.")