"""
03_dialogos_y_menus.py
-----------------------
Demostración de elementos estándar de sistemas de escritorio:
- Barra de menú principal con submenús, separadores y atajos.
- Cuadros de diálogo del sistema: messagebox (info, advertencia, confirmación).
- Cuadros de selección de archivos: filedialog (abrir y guardar).
- Selector de color de interfaz: colorchooser.
"""

import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from tkinter.scrolledtext import ScrolledText


def abrir_archivo():
    ruta = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                area_texto.delete("1.0", tk.END)
                area_texto.insert(tk.END, contenido)
            messagebox.showinfo("Éxito", f"Archivo cargado correctamente desde:\n{ruta}")
        except Exception as e:
            messagebox.showerror("Error al leer", f"No se pudo abrir el archivo:\n{e}")


def guardar_archivo():
    ruta = filedialog.asksaveasfilename(
        title="Guardar archivo como...",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        try:
            contenido = area_texto.get("1.0", tk.END)
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
            messagebox.showinfo("Guardado", "El archivo se ha guardado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo:\n{e}")


def cambiar_color_fondo():
    color = colorchooser.askcolor(title="Selecciona un color de fondo para el texto")
    # color retorna una tupla: ((r, g, b), '#hex')
    if color[1]:
        area_texto.config(bg=color[1])


def mostrar_alerta():
    messagebox.showwarning("Advertencia", "Esta es una alerta de advertencia informativa.")


def confirmar_salida():
    respuesta = messagebox.askyesno(
        "Confirmación de salida",
        "¿Estás seguro de que deseas cerrar la aplicación?"
    )
    if respuesta:
        ventana.destroy()


def acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Demostración de Menús y Diálogos con Tkinter\n"
        "Materia: Tópicos Avanzados de Programación\n"
        "Desarrollado con Python 3"
    )


# Ventana principal
ventana = tk.Tk()
ventana.title("03 - Menús y Cuadros de Diálogo")
ventana.geometry("600x420")

# 1. Barra de Menú Principal
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir archivo...", accelerator="Ctrl+O", command=abrir_archivo)
menu_archivo.add_command(label="Guardar como...", accelerator="Ctrl+S", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", accelerator="Alt+F4", command=confirmar_salida)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Personalizar
menu_personalizar = tk.Menu(barra_menu, tearoff=0)
menu_personalizar.add_command(label="Cambiar color del editor...", command=cambiar_color_fondo)
menu_personalizar.add_command(label="Disparar advertencia de prueba", command=mostrar_alerta)
barra_menu.add_cascade(label="Personalizar", menu=menu_personalizar)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Atajos de teclado vinculados
ventana.bind("<Control-o>", lambda event: abrir_archivo())
ventana.bind("<Control-s>", lambda event: guardar_archivo())

# Encabezado explicativo
tk.Label(
    ventana,
    text="Editor de Texto con Soporte para Diálogos de Sistema",
    font=("Segoe UI", 11, "bold"),
    pady=6
).pack()

# Área de texto desplazable (ScrolledText)
area_texto = ScrolledText(
    ventana,
    wrap="word",
    font=("Consolas", 11),
    padx=8,
    pady=8,
    bg="#ffffff",
    fg="#212121"
)
area_texto.pack(fill="both", expand=True, padx=15, pady=5)
area_texto.insert(tk.END, "¡Hola! Utiliza el menú superior 'Archivo' para abrir o guardar documentos,\n"
                          "o 'Personalizar' para cambiar el color de este lienzo con el selector de color.")

# Barra de estado inferior
barra_estado = tk.Label(
    ventana,
    text="Listo | Atajos: Ctrl+O (Abrir), Ctrl+S (Guardar)",
    bd=1,
    relief="sunken",
    anchor="w",
    font=("Segoe UI", 9),
    bg="#eeeeee",
    padx=5
)
barra_estado.pack(side="bottom", fill="x")

# Manejar el botón de cierre [X] de la ventana
ventana.protocol("WM_DELETE_WINDOW", confirmar_salida)

if __name__ == "__main__":
    ventana.mainloop()
