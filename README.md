# 🖥️ Aprendiendo Tkinter: Guía Práctica de Interfaces Gráficas en Python

> **Materia:** Tópicos Avanzados de Programación  
> **Autor:** [@keego124-design](https://github.com/keego124-design)  
> **Lenguaje:** Python 3.x (Tkinter Standard Library)  

---

## 📖 Descripción General

Este repositorio contiene una colección progresiva y didáctica de programas desarrollados con **Tkinter**, la biblioteca estándar de Python para la creación de Interfaces Gráficas de Usuario (GUI). 

El objetivo es demostrar el uso práctico de Tkinter desde sus conceptos más elementales (ventanas, botones, etiquetas y gestores de geometría) hasta patrones avanzados de desarrollo de software, tales como el enlace de eventos, dibujo vectorial con `Canvas` y la estructuración modular orientada a objetos (POO).

---

## 📁 Estructura del Proyecto

```text
aprendiendo-tkinter/
│
├── 01_hola_mundo_widgets.py    # Ventana básica, widgets esenciales y layouts (pack / grid)
├── 02_controles_y_variables.py   # Variables reactivas, Checkbuttons, Radiobuttons y Sliders
├── 03_dialogos_y_menus.py       # Menús superiores en cascada, ScrolledText y cuadros de diálogo
├── 04_canvas_y_graficos.py      # Gráficos vectoriales y dibujo interactivo con el mouse
├── 05_mini_app_poo.py          # Aplicación completa orientada a objetos con pestañas y tablas
├── .gitignore                   # Archivos y carpetas omitidas por Git
└── README.md                    # Documentación exhaustiva del proyecto
```

---

## 🔍 Detalle de los Módulos de Código

A continuación se detalla la función, conceptos clave y widgets implementados en cada archivo:

### 1. `01_hola_mundo_widgets.py` — *Fundamentos y Layouts*
- **Propósito:** Introducción a la creación de ventanas de escritorio y captura de texto.
- **Conceptos clave:**
  - Inicialización con `tk.Tk()`, asignación de título (`title`), dimensiones (`geometry`) y tamaño mínimo (`minsize`).
  - Uso de widgets esenciales: `Label` (texto), `Entry` (caja de texto para entrada de usuario) y `Button` (botones de acción).
  - Combinación de administradores de geometría: `pack()` para apilado vertical y `grid()` para formularios tabulares con filas y columnas.
  - Vinculación de funciones a botones mediante el parámetro `command`.

### 2. `02_controles_y_variables.py` — *Variables de Control y Reactividad*
- **Propósito:** Manejo de datos interactivos con sincronización de estado en tiempo real.
- **Conceptos clave:**
  - Uso de **Variables de Control** de Tkinter: `StringVar`, `IntVar`, `BooleanVar` y `DoubleVar`.
  - Suscripción de observadores reactivos con `trace_add("write", callback)` para refrescar la interfaz de forma inmediata cuando el usuario interactúa.
  - Widgets interactivos:
    - `Radiobutton`: Selección exclusiva entre varias opciones (ej. tema claro/oscuro).
    - `ttk.Combobox`: Lista desplegable de selección única.
    - `Checkbutton`: Casillas de verificación booleanas.
    - `Scale`: Deslizador numérico continuo (control de volumen).
    - `Spinbox`: Selector incremental con flechas numéricas.

### 3. `03_dialogos_y_menus.py` — *Navegación de Escritorio y Diálogos Modales*
- **Propósito:** Construcción de aplicaciones de escritorio completas con barra de menús del sistema y ventanas emergentes.
- **Conceptos clave:**
  - Menús en cascada con `tk.Menu`: Submenús (*Archivo*, *Personalizar*, *Ayuda*), separadores horizontales y atajos de teclado (`accelerator` y `bind("<Control-s>")`).
  - Diálogos estándar del módulo `messagebox`:
    - `showinfo()` (notificaciones informativas).
    - `showwarning()` (advertencias).
    - `showerror()` (mensajes de error).
    - `askyesno()` (confirmación de acciones críticas como salir).
  - Selector de archivos con `filedialog`: `askopenfilename()` para abrir documentos `.txt` y `asksaveasfilename()` para guardarlos.
  - Paleta de color con `colorchooser.askcolor()` para personalizar el fondo en tiempo real.
  - Área de texto con barras de desplazamiento integradas (`ScrolledText`).

### 4. `04_canvas_y_graficos.py` — *Gráficos Vectoriales y Eventos del Mouse*
- **Propósito:** Renderizado de primitivas 2D y manipulación de coordenadas en pantalla mediante eventos de puntero.
- **Conceptos clave:**
  - Uso intensivo del widget `Canvas`.
  - Dibujo de formas vectoriales: `create_rectangle()`, `create_oval()`, `create_polygon()`, `create_line()` y `create_text()`.
  - Detección y enlace de eventos de mouse:
    - `<Button-1>`: Clic inicial del botón izquierdo (guardar coordenadas de inicio).
    - `<B1-Motion>`: Arrastre del mouse con el botón presionado (trazado continuo de líneas).
    - `<ButtonRelease-1>`: Liberación del clic (finalizar trazo).
  - Pizarra interactiva estilo Paint con selector dinámico de color y grosor de pincel.

### 5. `05_mini_app_poo.py` — *Arquitectura Modular con Programación Orientada a Objetos*
- **Propósito:** Integración de todos los conceptos aprendidos en un sistema robusto, escalable y mantenible mediante POO.
- **Conceptos clave:**
  - Herencia de clase directa: `class AplicacionPrincipal(tk.Tk)`.
  - Modularización con `ttk.Notebook`: Organización de la aplicación en múltiples pestañas (*Gestor de Tareas* y *Bloc de Notas*).
  - Tablas de datos avanzadas con `ttk.Treeview`: Columnas formateadas, encabezados clicables, IDs autoincrementables y barra de desplazamiento vertical vinculada (`ttk.Scrollbar`).
  - Operaciones CRUD básicas: Alta de tareas con prioridad, actualización de estado a *Completada* y baja con confirmación modal.
  - Vinculación de eventos de teclado: `<Return>` para agregar tareas al presionar Enter y `<KeyRelease>` para actualizar contadores de palabras y caracteres en tiempo real.
  - Uso de `ttk.Style` para temas visuales modernos.

---

## 🚀 Requisitos e Instalación

### Prerrequisitos
- Tener instalado **Python 3.8** o superior.
- **Tkinter** viene incluido de forma nativa con la instalación estándar de Python en Windows y macOS, por lo que **no requiere instalar dependencias adicionales vía `pip`**.

### Instrucciones de Ejecución

1. **Clonar este repositorio:**
   ```bash
   git clone https://github.com/keego124-design/aprendiendo-thinter.git
   cd aprendiendo-thinter
   ```

2. **Ejecutar cualquiera de los ejemplos:**

   - *Ejemplo 1 (Fundamentos y Widgets):*
     ```powershell
     py 01_hola_mundo_widgets.py
     ```
   - *Ejemplo 2 (Controles y Variables Reactivas):*
     ```powershell
     py 02_controles_y_variables.py
     ```
   - *Ejemplo 3 (Menús y Diálogos):*
     ```powershell
     py 03_dialogos_y_menus.py
     ```
   - *Ejemplo 4 (Canvas y Gráficos):*
     ```powershell
     py 04_canvas_y_graficos.py
     ```
   - *Ejemplo 5 (Aplicación Completa POO):*
     ```powershell
     py 05_mini_app_poo.py
     ```
