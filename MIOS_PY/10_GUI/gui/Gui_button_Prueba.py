import pygame, sys

import tkinter as tk
from tkinter import PhotoImage

class BotonImagen:
    def __init__(self, master, imagen_path, comando=None):
        self.imagen = PhotoImage(file=imagen_path)
        self.boton = tk.Button(master, image=self.imagen, command=comando)
        self.boton.pack()

    def configurar_comando(self, nuevo_comando):
        """Permite cambiar la función que se ejecuta al presionar el botón."""
        self.boton.config(command=nuevo_comando)

# Función de ejemplo para el comando
def on_button_click():
    print("¡Botón de imagen presionado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Clase Botón de Imagen")

# Crear una instancia del botón de imagen
boton_imagen = BotonImagen(root, "ruta/a/tu/imagen.png", on_button_click)

# Ejecutar el bucle principal