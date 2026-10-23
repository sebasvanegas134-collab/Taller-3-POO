from abc import ABC, abstractmethod
import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ==================== CLASES MATEMÁTICAS (SIN CAMBIOS) ====================
class Figura3D(ABC):
    @abstractmethod
    def volumen(self) -> float:
        pass
    @abstractmethod
    def superficie(self) -> float:
        pass


class Esfera(Figura3D):
    def __init__(self, radio: float):
        self.radio = radio
    def volumen(self) -> float:
        return (4/3) * math.pi * (self.radio ** 3)
    def superficie(self):
        return 4*math.pi * self.radio**2 


class Cilindro(Figura3D):
    def __init__(self, radio: float, altura: float):
        self.radio = radio
        self.altura = altura
    def volumen(self) -> float:
        return math.pi * (self.radio ** 2) * self.altura
    def superficie(self):
        return 2*math.pi* self.radio * (self.altura+self.radio)


class Piramide(Figura3D):
    def __init__(self, base: float, altura: float, apotema: float):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    def volumen(self) -> float:
        return (1/3) * (self.base ** 2) * self.altura
    def superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema


class Cubo(Figura3D):
    def __init__(self, lado: float):
        self.lado = lado 
    def volumen(self):
        return self.lado**3
    def superficie(self):
        return 6 * self.lado**2


class Prisma(Figura3D, ABC):
    def __init__(self, altura:float):
        self.altura = altura

class PrismaRectangular(Prisma):
    def __init__(self, altura, largo:float, ancho:float):
        super().__init__(altura)
        self.largo = largo
        self.ancho = ancho
    def volumen(self):
        return self.largo * self.ancho * self.altura
    def superficie(self):
        return 2 * (self.largo * self.ancho + self.largo * self.altura + self.ancho * self.altura)
    

class PrismaTriangular(Prisma):
    def __init__(self, altura, baseT:float, alturaT:float):
        super().__init__(altura)
        self.baseT = baseT
        self.alturaT = alturaT
        self.perimetro = self.alturaT + self.baseT + math.sqrt(self.baseT**2 + self.alturaT**2)
    def volumen(self):
        return ((self.baseT * self.alturaT)/2) * self.altura
    def superficie(self):
        return (self.baseT * self.alturaT) + (self.perimetro * self.altura)


COLORES = {
    "fondo":        "#1e1e2e",
    "panel":        "#2a2a3c",
    "acento":       "#7c6cf0",
    "acento_hover": "#9a8cf7",
    "texto":        "#e4e4f0",
    "texto_suave":  "#a0a0b8",
    "exito":        "#4ade80",
    "error":        "#f87171",
    "entrada":      "#35354a",
}

# ==================== 3. CLASE BASE PARA VENTANAS ====================
class VentanaBase:
    def __init__(self, master, titulo):
        self.ventana = tk.Toplevel(master)
        self.ventana.title(titulo)
        self.ventana.geometry("400x520")
        self.ventana.configure(bg=COLORES["fondo"])
        self.ventana.resizable(False, False)
        
        self.contenedor = tk.Frame(self.ventana, bg=COLORES["fondo"])
        self.contenedor.pack(fill="both", expand=True, padx=25, pady=20)
        
        tk.Label(self.contenedor, text=titulo, font=("Segoe UI", 18, "bold"),
                 bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(0, 15))
                 
        self.canvas = tk.Canvas(self.contenedor, width=280, height=150, 
                                bg=COLORES["panel"], highlightthickness=1,
                                highlightbackground=COLORES["acento"], bd=0)
        self.canvas.pack(pady=(0, 15))

        self.frame_campos = tk.Frame(self.contenedor, bg=COLORES["panel"], 
                                     highlightbackground=COLORES["acento"], highlightthickness=1)
        self.frame_campos.pack(fill="x", pady=10)
        self.entradas = {}

        self.btn_calcular = tk.Button(self.contenedor, text="CALCULAR", font=("Segoe UI", 11, "bold"),
                                      bg=COLORES["acento"], fg="white", relief="flat", cursor="hand2",
                                      activebackground=COLORES["acento_hover"], command=self.calcular)
        self.btn_calcular.pack(fill="x", pady=10)

        self.panel_res = tk.Frame(self.contenedor, bg=COLORES["panel"], 
                                  highlightbackground=COLORES["acento"], highlightthickness=1)
        self.panel_res.pack(fill="x", pady=10)
        self.lbl_resultado = tk.Label(self.panel_res, text="Los resultados aparecerán aquí", 
                                      font=("Segoe UI", 11, "italic"), bg=COLORES["panel"], 
                                      fg=COLORES["texto_suave"], pady=15)
        self.lbl_resultado.pack()

    def crear_campo(self, nombre, fila):
        lbl = tk.Label(self.frame_campos, text=nombre, font=("Segoe UI", 10),
                       bg=COLORES["panel"], fg=COLORES["texto"])
        lbl.grid(row=fila, column=0, padx=(20, 10), pady=8, sticky="e")
        
        txt = tk.Entry(self.frame_campos, font=("Segoe UI", 10), width=15,
                       bg=COLORES["entrada"], fg=COLORES["texto"], insertbackground="white",
                       relief="flat", highlightthickness=1, highlightbackground=COLORES["acento"])
        txt.grid(row=fila, column=1, padx=(0, 20), pady=8, ipady=4)
        self.entradas[nombre] = txt

    def mostrar_resultado(self, v, s):
        self.lbl_resultado.config(text=f"Volumen (cm3):  {v:.2f}\nSuperficie (cm2):  {s:.2f}",
                                  fg=COLORES["exito"], font=("Segoe UI", 12, "bold"))

    def mostrar_error(self, mensaje="Error: Ingresa números válidos"):
        self.lbl_resultado.config(text=mensaje, 
                                  fg=COLORES["error"], font=("Segoe UI", 11, "bold"))

# ==================== 4. VENTANAS HIJAS ====================
class VentanaCilindro(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Cilindro")
        self.crear_campo("Radio (cms):", 0)
        self.crear_campo("Altura (cms):", 1)
        
        c = self.canvas
        c.create_rectangle(100, 30, 180, 120, outline=COLORES["acento"], width=2)
        c.create_oval(100, 15, 180, 45, outline=COLORES["acento"], width=2)
        c.create_oval(100, 105, 180, 135, outline=COLORES["texto_suave"], width=1)

    def calcular(self):
        try:
            r = float(self.entradas["Radio (cms):"].get())
            h = float(self.entradas["Altura (cms):"].get())
            if r < 0 or h < 0:
                self.mostrar_error("Error: No uses valores negativos")
                return
            fig = Cilindro(r, h)
            self.mostrar_resultado(fig.volumen(), fig.superficie())
        except ValueError:
            self.mostrar_error()

class VentanaEsfera(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Esfera")
        self.crear_campo("Radio (cms):", 0)
        
        c = self.canvas
        c.create_oval(90, 15, 190, 115, outline=COLORES["acento"], width=2)
        c.create_oval(90, 50, 190, 80, outline=COLORES["texto_suave"], width=1)

    def calcular(self):
        try:
            r = float(self.entradas["Radio (cms):"].get())
            if r < 0:
                self.mostrar_error("Error: No uses valores negativos")
                return
            fig = Esfera(r)
            self.mostrar_resultado(fig.volumen(), fig.superficie())
        except ValueError:
            self.mostrar_error()

class VentanaPiramide(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Pirámide")
        self.ventana.geometry("400x560") 
        self.crear_campo("Base (cms):", 0)
        self.crear_campo("Altura (cms):", 1)
        self.crear_campo("Apotema (cms):", 2)
        
        c = self.canvas
        c.create_polygon(60, 120, 220, 120, 140, 20, outline=COLORES["acento"], width=2, fill="")
        c.create_line(60, 120, 100, 100, fill=COLORES["texto_suave"], width=1)
        c.create_line(220, 120, 100, 100, fill=COLORES["texto_suave"], width=1)
        c.create_line(140, 20, 100, 100, fill=COLORES["texto_suave"], width=1)
        
    def calcular(self):
        try:
            b = float(self.entradas["Base (cms):"].get())
            h = float(self.entradas["Altura (cms):"].get())
            a = float(self.entradas["Apotema (cms):"].get())
            if b < 0 or h < 0 or a < 0:
                self.mostrar_error("Error: No uses valores negativos")
                return
            fig = Piramide(b, h, a)
            self.mostrar_resultado(fig.volumen(), fig.superficie())
        except ValueError:
            self.mostrar_error()

class VentanaCubo(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Cubo")
        self.crear_campo("Lado (cms):", 0)
        
        c = self.canvas
        c.create_rectangle(105, 40, 175, 110, outline=COLORES["acento"], width=2)
        c.create_line(105, 40, 130, 15, fill=COLORES["texto_suave"], width=1)
        c.create_line(175, 40, 200, 15, fill=COLORES["texto_suave"], width=1)
        c.create_line(175, 110, 200, 85, fill=COLORES["texto_suave"], width=1)
        c.create_line(130, 15, 200, 15, fill=COLORES["texto_suave"], width=1)
        c.create_line(200, 15, 200, 85, fill=COLORES["texto_suave"], width=1)

    def calcular(self):
        try:
            l = float(self.entradas["Lado (cms):"].get())
            if l < 0:
                self.mostrar_error("Error: No uses valores negativos")
                return
            fig = Cubo(l)
            self.mostrar_resultado(fig.volumen(), fig.superficie())
        except ValueError:
            self.mostrar_error()

class VentanaPrismaRect(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Prisma Rectangular")
        self.ventana.geometry("400x560")
        self.crear_campo("Largo (cms):", 0)
        self.crear_campo("Ancho (cms):", 1)
        self.crear_campo("Altura (cms):", 2)
        
        c = self.canvas
        c.create_rectangle(70, 45, 210, 105, outline=COLORES["acento"], width=2)
        c.create_line(70, 45, 90, 25, fill=COLORES["texto_suave"], width=1)
        c.create_line(210, 45, 230, 25, fill=COLORES["texto_suave"], width=1)
        c.create_line(90, 25, 230, 25, fill=COLORES["texto_suave"], width=1)
        c.create_line(230, 25, 230, 85, fill=COLORES["texto_suave"], width=1)
        c.create_line(210, 105, 230, 85, fill=COLORES["texto_suave"], width=1)

    def calcular(self):
        try:
            l = float(self.entradas["Largo (cms):"].get())
            a = float(self.entradas["Ancho (cms):"].get())
            h = float(self.entradas["Altura (cms):"].get())
            if l < 0 or a < 0 or h < 0:
                self.mostrar_error("Error: No uses valores negativos")
                return
            fig = PrismaRectangular(h, l, a)
            self.mostrar_resultado(fig.volumen(), fig.superficie())
        except ValueError:
            self.mostrar_error()

class VentanaPrismaTriangular(VentanaBase):
    def __init__(self, master):
        super().__init__(master, "Prisma Triangular")
        self.ventana.geometry("400x560")
        self.crear_campo("Base Triángulo:", 0)
        self.crear_campo("Altura Triángulo:", 1)
        self.crear_campo("Altura Prisma:", 2)
        
        c = self.canvas
        c.create_polygon(80, 100, 200, 100, 140, 30, outline=COLORES["acento"], width=2, fill="")
        c.create_line(80, 100, 100, 80, fill=COLORES["texto_suave"], width=1)
        c.create_line(200, 100, 220, 80, fill=COLORES["texto_suave"], width=1)
        c.create_line(100, 80, 220, 80, fill=COLORES["texto_suave"], width=1)
        c.create_line(220, 80, 140, 30, fill=COLORES["texto_suave"], width=1)

    def calcular(self):
        try:
            b = float(self.entradas["Base Triángulo:"].get())
            at = float(self.entradas["Altura Triángulo:"].get())
            hp = float(self.entradas["Altura Prisma:"].get())
            if b < 0 or at < 0 or hp < 0:
                self.mostrar_error("Error: No uses valores negativos")
                return
            fig = PrismaTriangular(hp, b, at)
            self.mostrar_resultado(fig.volumen(), fig.superficie())
        except ValueError:
            self.mostrar_error()
            
# ==================== 5. VENTANA PRINCIPAL ====================
class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora 3D - Principal")
        self.ventana.geometry("500x220")
        self.ventana.configure(bg=COLORES["fondo"])
        self.ventana.resizable(False, False)

        tk.Label(ventana, text="Selecciona una Figura", font=("Segoe UI", 14, "bold"),
                 bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(25, 15))

        # Dividimos en dos filas de botones para que no queden apretados
        frame_fila1 = tk.Frame(ventana, bg=COLORES["fondo"])
        frame_fila1.pack(pady=5)
        frame_fila2 = tk.Frame(ventana, bg=COLORES["fondo"])
        frame_fila2.pack(pady=5)

        # Función auxiliar rápida para crear botones (evita repetir código)
        def crear_btn(padre, texto, comando):
            return tk.Button(padre, text=texto, font=("Segoe UI", 9, "bold"),
                             bg=COLORES["panel"], fg=COLORES["texto"], width=14, pady=8,
                             relief="flat", cursor="hand2", command=comando)

        
        crear_btn(frame_fila1, "Cilindro", lambda: VentanaCilindro(self.ventana)).pack(side="left", padx=5)
        crear_btn(frame_fila1, "Esfera", lambda: VentanaEsfera(self.ventana)).pack(side="left", padx=5)
        crear_btn(frame_fila1, "Pirámide", lambda: VentanaPiramide(self.ventana)).pack(side="left", padx=5)
        crear_btn(frame_fila2, "Cubo", lambda: VentanaCubo(self.ventana)).pack(side="left", padx=5)
        crear_btn(frame_fila2, "Prisma Rect.", lambda: VentanaPrismaRect(self.ventana)).pack(side="left", padx=5)
        crear_btn(frame_fila2, "Prisma Triang.", lambda: VentanaPrismaTriangular(self.ventana)).pack(side="left", padx=5)


if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = VentanaPrincipal(ventana_raiz)
    ventana_raiz.mainloop()