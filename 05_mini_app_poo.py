"""
05_mini_app_poo.py
-------------------
Aplicación integral estructurada bajo Programación Orientada a Objetos (POO):
- Arquitectura basada en herencia (tk.Tk).
- Pestañas con ttk.Notebook.
- Tablas de datos avanzadas con ttk.Treeview y barras de desplazamiento (Scrollbar).
- Estilos modernos ttk (ttk.Style).
- Pestaña 1: Gestor interactivo de tareas (agregar, completar, eliminar con confirmación).
- Pestaña 2: Bloc de notas con contador de caracteres y palabras en vivo.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("05 - Mini Aplicación POO (Gestor de Tareas y Notas)")
        self.geometry("750x520")
        self.minsize(650, 450)

        # Aplicar tema ttk moderno
        self.estilo = ttk.Style(self)
        if "clam" in self.estilo.theme_names():
            self.estilo.theme_use("clam")

        self._configurar_interfaz()

    def _configurar_interfaz(self):
        # Encabezado
        lbl_titulo = tk.Label(
            self,
            text="Sistema Integrado de Tareas y Notas",
            font=("Segoe UI", 14, "bold"),
            bg="#263238",
            fg="white",
            pady=10
        )
        lbl_titulo.pack(fill="x")

        # Contenedor de pestañas
        self.cuaderno = ttk.Notebook(self)
        self.cuaderno.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Tareas
        self.tab_tareas = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.tab_tareas, text=" 📋 Gestor de Tareas ")
        self._construir_tab_tareas()

        # Pestaña 2: Notas
        self.tab_notas = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.tab_notas, text=" 📝 Bloc de Notas ")
        self._construir_tab_notas()

    # -------------------------------------------------------------
    # PESTAÑA 1: GESTOR DE TAREAS (TREEVIEW)
    # -------------------------------------------------------------
    def _construir_tab_tareas(self):
        # Formulario de entrada superior
        frame_input = ttk.LabelFrame(self.tab_tareas, text=" Nueva Tarea ", padding=10)
        frame_input.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_input, text="Descripción:").grid(row=0, column=0, padx=5, sticky="w")
        self.entry_tarea = ttk.Entry(frame_input, width=35)
        self.entry_tarea.grid(row=0, column=1, padx=5, sticky="w")
        self.entry_tarea.bind("<Return>", lambda e: self.agregar_tarea())

        ttk.Label(frame_input, text="Prioridad:").grid(row=0, column=2, padx=5, sticky="w")
        self.combo_prioridad = ttk.Combobox(
            frame_input,
            values=["Alta", "Media", "Baja"],
            state="readonly",
            width=10
        )
        self.combo_prioridad.set("Media")
        self.combo_prioridad.grid(row=0, column=3, padx=5, sticky="w")

        btn_agregar = ttk.Button(frame_input, text="Agregar", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=4, padx=10)

        # Tabla Treeview para mostrar tareas
        frame_tabla = ttk.Frame(self.tab_tareas)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        columnas = ("id", "descripcion", "prioridad", "estado")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")

        self.tree.heading("id", text="#")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.heading("prioridad", text="Prioridad")
        self.tree.heading("estado", text="Estado")

        self.tree.column("id", width=40, anchor="center")
        self.tree.column("descripcion", width=360)
        self.tree.column("prioridad", width=100, anchor="center")
        self.tree.column("estado", width=120, anchor="center")

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones de acción inferiores
        frame_acciones = ttk.Frame(self.tab_tareas, padding=5)
        frame_acciones.pack(fill="x", padx=10)

        ttk.Button(frame_acciones, text="✓ Marcar como Completada", command=self.completar_tarea).pack(side="left", padx=5)
        ttk.Button(frame_acciones, text="🗑 Eliminar Tarea", command=self.eliminar_tarea).pack(side="left", padx=5)

        self.contador_id = 1
        # Cargar tareas de demostración
        self._insertar_tarea_tabla("Revisar tema de Tkinter", "Alta", "Pendiente")
        self._insertar_tarea_tabla("Diseñar interfaz para clase", "Media", "Completada")

    def _insertar_tarea_tabla(self, desc, prioridad, estado):
        self.tree.insert("", "end", values=(self.contador_id, desc, prioridad, estado))
        self.contador_id += 1

    def agregar_tarea(self):
        desc = self.entry_tarea.get().strip()
        if not desc:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una descripción para la tarea.")
            return

        prioridad = self.combo_prioridad.get()
        self._insertar_tarea_tabla(desc, prioridad, "Pendiente")
        self.entry_tarea.delete(0, tk.END)

    def completar_tarea(self):
        item_sel = self.tree.selection()
        if not item_sel:
            messagebox.showinfo("Aviso", "Selecciona una tarea de la tabla primero.")
            return

        valores = list(self.tree.item(item_sel, "values"))
        valores[3] = "Completada"
        self.tree.item(item_sel, values=valores)

    def eliminar_tarea(self):
        item_sel = self.tree.selection()
        if not item_sel:
            messagebox.showinfo("Aviso", "Selecciona una tarea de la tabla para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar la tarea seleccionada?")
        if confirmar:
            self.tree.delete(item_sel)

    # -------------------------------------------------------------
    # PESTAÑA 2: BLOC DE NOTAS
    # -------------------------------------------------------------
    def _construir_tab_notas(self):
        frame_contenedor = ttk.Frame(self.tab_notas, padding=10)
        frame_contenedor.pack(fill="both", expand=True)

        self.txt_notas = tk.Text(
            frame_contenedor,
            wrap="word",
            font=("Segoe UI", 11),
            padx=10,
            pady=10,
            relief="solid",
            bd=1
        )
        self.txt_notas.pack(fill="both", expand=True)
        self.txt_notas.insert("1.0", "Escribe tus apuntes o notas aquí...\nEl contador inferior se actualizará en tiempo real.")
        self.txt_notas.bind("<KeyRelease>", self._actualizar_estadisticas_texto)

        self.lbl_stats = ttk.Label(frame_contenedor, text="Palabras: 0 | Caracteres: 0", font=("Segoe UI", 9, "italic"))
        self.lbl_stats.pack(anchor="e", pady=5)
        self._actualizar_estadisticas_texto()

    def _actualizar_estadisticas_texto(self, event=None):
        contenido = self.txt_notas.get("1.0", "end-1c")
        caracteres = len(contenido)
        palabras = len(contenido.split()) if contenido.strip() else 0
        self.lbl_stats.config(text=f"Palabras: {palabras} | Caracteres: {caracteres}")


if __name__ == "__main__":
    app = AplicacionPrincipal()
    app.mainloop()
