"""
02_controles_y_variables.py
----------------------------
Demostración de controles interactivos y variables reactivas en Tkinter:
- Variables de control: StringVar, IntVar, BooleanVar, DoubleVar.
- Widgets de selección: Checkbutton, Radiobutton, ttk.Combobox, Scale y Spinbox.
- Actualización dinámica del estado en tiempo real.
"""

import tkinter as tk
from tkinter import ttk


def actualizar_resumen(*args):
    """Función reactiva que lee las variables de control y actualiza la vista."""
    sistema = var_sistema.get()
    notificaciones = "Activadas" if var_notificaciones.get() else "Desactivadas"
    tema = var_tema.get()
    volumen = int(var_volumen.get())
    fuente_tam = var_tamanio_fuente.get()

    resumen = (
        f"--- Configuración Actual ---\n"
        f"• Sistema Operativo: {sistema}\n"
        f"• Tema de Interfaz:  {tema}\n"
        f"• Notificaciones:   {notificaciones}\n"
        f"• Nivel de Volumen: {volumen}%\n"
        f"• Tamaño de Fuente: {fuente_tam} pt"
    )
    lbl_resultado.config(text=resumen)


# Ventana principal
ventana = tk.Tk()
ventana.title("02 - Controles y Variables Reactivas")
ventana.geometry("520x540")
ventana.config(bg="#fafafa")

# Variables reactivas de Tkinter
var_sistema = tk.StringVar(value="Linux")
var_notificaciones = tk.BooleanVar(value=True)
var_tema = tk.StringVar(value="Claro")
var_volumen = tk.DoubleVar(value=75.0)
var_tamanio_fuente = tk.IntVar(value=12)

# Suscribir variables para que al cambiar actualicen automáticamente el resumen
var_sistema.trace_add("write", actualizar_resumen)
var_notificaciones.trace_add("write", actualizar_resumen)
var_tema.trace_add("write", actualizar_resumen)
var_volumen.trace_add("write", actualizar_resumen)
var_tamanio_fuente.trace_add("write", actualizar_resumen)

# Encabezado
tk.Label(
    ventana,
    text="Panel de Preferencias de Usuario",
    font=("Segoe UI", 13, "bold"),
    bg="#fafafa",
    fg="#303f9f"
).pack(pady=10)

# Contenedor con borde
panel = tk.LabelFrame(ventana, text=" Opciones Disponibles ", font=("Segoe UI", 10, "bold"), bg="#fafafa", padx=15, pady=10)
panel.pack(padx=20, pady=5, fill="both")

# 1. Radiobuttons: Selección única de Tema
tk.Label(panel, text="Tema visual:", font=("Segoe UI", 10, "bold"), bg="#fafafa").grid(row=0, column=0, sticky="w", pady=4)
frame_radio = tk.Frame(panel, bg="#fafafa")
frame_radio.grid(row=0, column=1, sticky="w", pady=4)
tk.Radiobutton(frame_radio, text="Claro", variable=var_tema, value="Claro", bg="#fafafa").pack(side="left", padx=5)
tk.Radiobutton(frame_radio, text="Oscuro", variable=var_tema, value="Oscuro", bg="#fafafa").pack(side="left", padx=5)
tk.Radiobutton(frame_radio, text="Sistema", variable=var_tema, value="Sistema", bg="#fafafa").pack(side="left", padx=5)

# 2. Combobox (ttk): Lista desplegable de SO
tk.Label(panel, text="Sistema preferido:", font=("Segoe UI", 10, "bold"), bg="#fafafa").grid(row=1, column=0, sticky="w", pady=4)
combo_so = ttk.Combobox(panel, textvariable=var_sistema, values=["Windows", "macOS", "Linux", "BSD"], state="readonly", width=18)
combo_so.grid(row=1, column=1, sticky="w", pady=4)

# 3. Checkbutton: Casilla booleana
tk.Label(panel, text="Alertas:", font=("Segoe UI", 10, "bold"), bg="#fafafa").grid(row=2, column=0, sticky="w", pady=4)
check_notif = tk.Checkbutton(panel, text="Recibir notificaciones por correo", variable=var_notificaciones, bg="#fafafa")
check_notif.grid(row=2, column=1, sticky="w", pady=4)

# 4. Scale: Control deslizante de volumen (0 - 100)
tk.Label(panel, text="Volumen:", font=("Segoe UI", 10, "bold"), bg="#fafafa").grid(row=3, column=0, sticky="w", pady=4)
slider_vol = tk.Scale(
    panel,
    from_=0,
    to=100,
    orient="horizontal",
    variable=var_volumen,
    bg="#fafafa",
    troughcolor="#e0e0e0",
    length=200,
    showvalue=True
)
slider_vol.grid(row=3, column=1, sticky="w", pady=4)

# 5. Spinbox: Selector de número con flechas arriba/abajo
tk.Label(panel, text="Tamaño fuente:", font=("Segoe UI", 10, "bold"), bg="#fafafa").grid(row=4, column=0, sticky="w", pady=4)
spin_fuente = tk.Spinbox(panel, from_=8, to=32, textvariable=var_tamanio_fuente, width=8)
spin_fuente.grid(row=4, column=1, sticky="w", pady=4)

# Cuadro para mostrar resumen en tiempo real
frame_resumen = tk.LabelFrame(ventana, text=" Estado en Tiempo Real ", font=("Segoe UI", 10, "bold"), bg="#f1f8e9", padx=10, pady=10)
frame_resumen.pack(padx=20, pady=15, fill="both", expand=True)

lbl_resultado = tk.Label(
    frame_resumen,
    text="",
    font=("Consolas", 10),
    justify="left",
    bg="#f1f8e9",
    fg="#1b5e20"
)
lbl_resultado.pack(anchor="w")

# Inicializar resumen al arrancar
actualizar_resumen()

if __name__ == "__main__":
    ventana.mainloop()
