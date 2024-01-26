import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()

def convertir_vel():
    distancia = float(caja_temp_celsius.get())
    tiempo = float(caja_temp_celsius.get())
    vel = distancia/tiempo
    etiqueta_vel.config(text=f"Velocidad media en m/s: {vel}")


ventana.title("Conversor de velocidad media")
ventana.config(width=1000, height=1000)

etiqueta_distancia = ttk.Label(text="Distancia en metros:")
etiqueta_distancia.place(x=22, y=60)

etiqueta_tiempo = ttk.Label(text="Tiempo en segundos:")
etiqueta_tiempo.place(x=20, y=20)

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)

boton_convertir = ttk.Button(text="Convertir", command=convertir_vel)
boton_convertir.place(x=20, y=60)

etiqueta_vel = ttk.Label(text="Temperatura en K: n/a")
etiqueta_vel.place(x=20, y=120)

ventana.mainloop()

