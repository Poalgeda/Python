#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

var1= "A quién madruga Dios ayuda."
frase_minusculas = var1.lower()
words_verificar = ["quién", "dios", "ayuda", "sol"]
words_verificar = [palabra.lower() for palabra in words_verificar]
for palabra in words_verificar:
    if palabra in frase_minusculas:
        indice = frase_minusculas.index(palabra)
        print(f"La palabra '{palabra}' está en la posición de índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no está en la frase.")
input()