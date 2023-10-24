#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.
stc="A quién madruga dios ayuda: "
var1=input("introduce una palabra: ")
indice=stc.find(var1)
if var1 in stc:
    print(f"La palabra esta en la frase y el índice es {indice} ")
else:
    print("La palabra no está en la frase")