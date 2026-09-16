"""
01_hola_mundo_widgets.py
-------------------------
Demostración básica de Tkinter:
- Creación de ventana principal (title, geometry, resizable).
- Widgets fundamentales: Label, Entry y Button.
- Administradores de geometría: pack() y grid().
- Captura de eventos mediante comandos (command).
"""

import tkinter as tk
from tkinter import ttk


def saludar():
    nombre = entrada_nombre.get().strip()
    if nombre:
        etiqueta_saludo.config(
            text=f"¡Hola, {nombre}! Bienvenido a Tkinter.",
            fg="#1b5e20"
        )
    else:
        etiqueta_saludo.config(
            text="Por favor, escribe tu nombre primero.",
            fg="#b71c1c"
        )


def limpiar():
    entrada_nombre.delete(0, tk.END)
    etiqueta_saludo.config(text="Escribe tu nombre y presiona 'Saludar'", fg="#424242")


# 1. Ventana Principal
ventana = tk.Tk()
ventana.title("01 - Hola Mundo y Widgets Básicos")
ventana.geometry("450x300")
ventana.minsize(400, 250)
ventana.config(bg="#f5f5f5")

# 2. Título superior usando pack()
etiqueta_titulo = tk.Label(
    ventana,
    text="Mi Primera Aplicación GUI con Tkinter",
    font=("Arial", 14, "bold"),
    bg="#f5f5f5",
    fg="#0d47a1"
)
etiqueta_titulo.pack(pady=15)

# 3. Contenedor (Frame) para organizar formulario con grid()
frame_formulario = tk.Frame(ventana, bg="#f5f5f5")
frame_formulario.pack(pady=10)

etiqueta_instruccion = tk.Label(
    frame_formulario,
    text="Nombre:",
    font=("Arial", 11),
    bg="#f5f5f5"
)
etiqueta_instruccion.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entrada_nombre = tk.Entry(
    frame_formulario,
    font=("Arial", 11),
    width=20,
    relief="groove",
    bd=2
)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
entrada_nombre.focus()  # Pone el cursor directamente en este campo

# 4. Botones de acción organizados con grid()
frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=10)

boton_saludar = tk.Button(
    frame_botones,
    text="Saludar",
    font=("Arial", 10, "bold"),
    bg="#1976d2",
    fg="white",
    padx=10,
    pady=5,
    cursor="hand2",
    command=saludar
)
boton_saludar.grid(row=0, column=0, padx=5)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    font=("Arial", 10),
    bg="#e0e0e0",
    fg="#212121",
    padx=10,
    pady=5,
    cursor="hand2",
    command=limpiar
)
boton_limpiar.grid(row=0, column=1, padx=5)

# 5. Etiqueta de resultado
etiqueta_saludo = tk.Label(
    ventana,
    text="Escribe tu nombre y presiona 'Saludar'",
    font=("Arial", 11, "italic"),
    bg="#f5f5f5",
    fg="#424242"
)
etiqueta_saludo.pack(pady=15)

# Bucle principal de eventos
if __name__ == "__main__":
    ventana.mainloop()
