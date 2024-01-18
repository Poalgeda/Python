import tkinter as tk
from tkinter import ttk  
#Ahora vamos a dar un título y un tamaño a la ventana, vía los métodos title() y config()
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)
ventana.mainloop
#Empecemos por mostrar un mensaje en la ventana que indique al usuario que debe ingresar la temperatura en grados Celsius,
# para lo cual podemos usar un control o widget llamado etiqueta. La etiqueta está representada en Tk por la clase ttk.Label.
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)
etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.place(x=20, y=20)

#LINK: https://recursospython.com/guias-y-manuales/introduccion-a-tkinter/