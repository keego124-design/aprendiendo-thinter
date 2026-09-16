"""
04_canvas_y_graficos.py
-----------------------
Demostración de capacidades gráficas y eventos de mouse con Canvas:
- Creación y manipulación del widget Canvas.
- Dibujo de formas geométricas vectoriales (rectángulos, elipses, líneas, texto).
- Vinculación de eventos de mouse (<Button-1>, <B1-Motion>).
- Mini pizarra de dibujo libre estilo Paint con grosor y paleta de colores.
"""

import tkinter as tk
from tkinter import colorchooser


class PizarraGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("04 - Canvas y Eventos del Mouse")
        self.master.geometry("700x560")
        self.master.config(bg="#e0e0e0")

        self.color_actual = "#d32f2f"  # Rojo inicial
        self.grosor_actual = 3
        self.x_previo = None
        self.y_previo = None

        self._crear_panel_herramientas()
        self._crear_canvas()
        self.dibujar_figuras_demostracion()

    def _crear_panel_herramientas(self):
        panel = tk.Frame(self.master, bg="#f5f5f5", padx=10, pady=8, bd=1, relief="ridge")
        panel.pack(side="top", fill="x")

        # Botón elegir color
        self.btn_color = tk.Button(
            panel,
            text="Color del Trazo",
            bg=self.color_actual,
            fg="white",
            font=("Segoe UI", 9, "bold"),
            command=self.seleccionar_color,
            cursor="hand2"
        )
        self.btn_color.pack(side="left", padx=5)

        # Selector de grosor
        tk.Label(panel, text="Grosor:", font=("Segoe UI", 9), bg="#f5f5f5").pack(side="left", padx=(10, 2))
        self.scale_grosor = tk.Scale(
            panel,
            from_=1,
            to=15,
            orient="horizontal",
            length=100,
            command=self.cambiar_grosor,
            bg="#f5f5f5"
        )
        self.scale_grosor.set(self.grosor_actual)
        self.scale_grosor.pack(side="left", padx=5)

        # Botones de acción
        tk.Button(
            panel,
            text="Dibujar Figuras Demo",
            command=self.dibujar_figuras_demostracion,
            cursor="hand2"
        ).pack(side="left", padx=10)

        tk.Button(
            panel,
            text="Limpiar Lienzo",
            command=self.limpiar_lienzo,
            bg="#ffebee",
            fg="#c62828",
            cursor="hand2"
        ).pack(side="right", padx=5)

    def _crear_canvas(self):
        self.canvas = tk.Canvas(self.master, bg="#ffffff", cursor="pencil")
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)

        # Eventos para dibujo interactivo
        self.canvas.bind("<Button-1>", self.iniciar_trazo)
        self.canvas.bind("<B1-Motion>", self.trazar_linea)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_trazo)

    def seleccionar_color(self):
        color = colorchooser.askcolor(color=self.color_actual, title="Elige un color para dibujar")
        if color[1]:
            self.color_actual = color[1]
            self.btn_color.config(bg=self.color_actual)

    def cambiar_grosor(self, valor):
        self.grosor_actual = int(valor)

    def iniciar_trazo(self, event):
        self.x_previo = event.x
        self.y_previo = event.y

    def trazar_linea(self, event):
        if self.x_previo and self.y_previo:
            self.canvas.create_line(
                self.x_previo,
                self.y_previo,
                event.x,
                event.y,
                fill=self.color_actual,
                width=self.grosor_actual,
                capstyle=tk.ROUND,
                smooth=True
            )
            self.x_previo = event.x
            self.y_previo = event.y

    def finalizar_trazo(self, event):
        self.x_previo = None
        self.y_previo = None

    def dibujar_figuras_demostracion(self):
        """Dibuja ejemplos de formas vectoriales de Tkinter."""
        # Rectángulo
        self.canvas.create_rectangle(30, 30, 160, 120, fill="#bbdefb", outline="#1976d2", width=2)
        self.canvas.create_text(95, 75, text="Rectángulo", font=("Segoe UI", 10, "bold"), fill="#0d47a1")

        # Círculo / Óvalo
        self.canvas.create_oval(190, 30, 300, 140, fill="#c8e6c9", outline="#388e3c", width=2)
        self.canvas.create_text(245, 85, text="Círculo", font=("Segoe UI", 10, "bold"), fill="#1b5e20")

        # Polígono / Triángulo
        self.canvas.create_polygon(330, 130, 390, 30, 450, 130, fill="#ffe0b2", outline="#f57c00", width=2)
        self.canvas.create_text(390, 95, text="Polígono", font=("Segoe UI", 10, "bold"), fill="#e65100")

        # Texto informativo en el canvas
        self.canvas.create_text(
            350, 175,
            text="¡Dibuja libremente en cualquier parte del lienzo arrastrando el mouse!",
            font=("Segoe UI", 11, "italic"),
            fill="#616161"
        )

    def limpiar_lienzo(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    raiz = tk.Tk()
    app = PizarraGrafica(raiz)
    raiz.mainloop()
