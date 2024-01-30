import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()

def convertir_vel():
    distancia = float(caja_distancia.get())
    tiempo = float(caja_tiempo.get())
    vel = distancia/tiempo
    etiqueta_vel.config(text=f"Velocidad media: {vel} m/s")


ventana.title("Conversor de velocidad media")
ventana.config(width=1000, height=1000)

etiqueta_distancia = ttk.Label(text="Distancia en metros:")
etiqueta_distancia.place(x=22, y=60)

etiqueta_tiempo = ttk.Label(text="Tiempo en segundos:")
etiqueta_tiempo.place(x=20, y=20)

caja_tiempo = ttk.Entry()
caja_tiempo.place(x=140, y=20, width=60)

caja_distancia = ttk.Entry()
caja_distancia.place(x=140, y=60, width=60)

boton_convertir = ttk.Button(text="Convertir", command=convertir_vel)
boton_convertir.place(x=20, y=100)

etiqueta_vel = ttk.Label(text="Velocidad en m/s: n/a")
etiqueta_vel.place(x=20, y=130)

ventana.mainloop()

