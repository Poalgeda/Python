import tkinter as tk
from tkinter import ttk  



ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)
etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.place(x=20, y=20)