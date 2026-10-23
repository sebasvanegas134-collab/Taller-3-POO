import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import math

# ==================== BACKEND ====================
class Notas:
    def __init__(self, N1:float, N2:float, N3:float, N4:float, N5:float):
        self.listaNotas = [N1, N2, N3, N4, N5] # Adaptado al atributo listaNotas del diagrama
        
    def calcularPromedio(self):
        return sum(self.listaNotas) / 5
        
    def calcularDesviacion(self):
        promedio = self.calcularPromedio()
        sumaCuadrados = sum((x - promedio)**2 for x in self.listaNotas)
        varianza = sumaCuadrados / 4 # N-1 para la muestra
        return math.sqrt(varianza)
        
    def calcularMenor(self):
        return min(self.listaNotas)
        
    def calcularMayor(self):
        return max(self.listaNotas)

class CamposVaciosError(Exception):
    pass
class NotaFueraDeRangoError(Exception):
    pass

# ==================== FRONTEND ====================
class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Notas")
        self.ventana.geometry("450x390")
        self.ventana.configure(bg="#1e1e2e") 
        self.ventana.resizable(False, False)
        self.notas = None
        self.inicio()
        
    def inicio(self):
        # Estilos globales modernos (TTK)
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.estilo.configure('.', background='#1e1e2e', foreground='#cdd6f4')
        self.estilo.configure('TLabel', font=('Segoe UI', 10, 'bold'), foreground='#a6adc8')
        self.estilo.configure('Calcular.TButton', font=('Segoe UI', 10, 'bold'), background='#89b4fa', foreground='#11111b', borderwidth=0)
        self.estilo.map('Calcular.TButton', background=[('active', '#b4befe')])
        self.estilo.configure('Limpiar.TButton', font=('Segoe UI', 10, 'bold'), background='#f38ba8', foreground='#11111b', borderwidth=0)
        self.estilo.map('Limpiar.TButton', background=[('active', '#eba0ac')])

        # Título
        tk.Label(self.ventana, text="ANÁLISIS DE NOTAS", font=("Segoe UI", 14, "bold"), bg="#1e1e2e", fg="#89b4fa").pack(pady=20)

        # Formulario
        self.frame_formulario = tk.Frame(self.ventana, bg="#1e1e2e")
        self.frame_formulario.pack(pady=5)
        
        self.entradas = []
        for i in range(5):
            ttk.Label(self.frame_formulario, text=f"Nota {i+1}:").grid(row=i, column=0, padx=15, pady=6, sticky="e")
            entry = tk.Entry(self.frame_formulario, font=("Segoe UI", 11), bg="#313244", fg="#cdd6f4", bd=0, insertbackground="white", justify="center", width=14)
            entry.grid(row=i, column=1, padx=15, pady=6, ipady=4)
            self.entradas.append(entry)

        self.campoNota1, self.campoNota2, self.campoNota3, self.campoNota4, self.campoNota5 = self.entradas

        # Botones
        self.frame_botones = tk.Frame(self.ventana, bg="#1e1e2e")
        self.frame_botones.pack(pady=20)

        self.btn_calcular = ttk.Button(self.frame_botones, text="Calcular", style='Calcular.TButton', command=self.actionPerformed, cursor="hand2")
        self.btn_calcular.pack(side=tk.LEFT, padx=10, ipadx=12, ipady=5)

        self.btn_limpiar = ttk.Button(self.frame_botones, text="Limpiar", style='Limpiar.TButton', command=self.limpiar, cursor="hand2")
        self.btn_limpiar.pack(side=tk.LEFT, padx=10, ipadx=12, ipady=5)

        # Contenedor de Resultados 
        self.frame_resultados = tk.Frame(self.ventana, bg="#313244", bd=0)
        self.lbl_resultado = tk.Label(self.frame_resultados, text="", font=("Segoe UI", 11, "bold"), bg="#313244", fg="#a6e3a1")
        self.lbl_resultado.pack(pady=6)
        self.lbl_resultado2 = tk.Label(self.frame_resultados, text="", font=("Segoe UI", 10), bg="#313244", fg="#cdd6f4")
        self.lbl_resultado2.pack(pady=3)
        self.lbl_resultado3 = tk.Label(self.frame_resultados, text="", font=("Segoe UI", 10), bg="#313244", fg="#cdd6f4")
        self.lbl_resultado3.pack(pady=3)
        self.lbl_resultado4 = tk.Label(self.frame_resultados, text="", font=("Segoe UI", 10), bg="#313244", fg="#cdd6f4")
        self.lbl_resultado4.pack(pady=(3, 10))

    def animar_ventana(self, altura_objetivo):
        altura_actual = self.ventana.winfo_height()
        paso = 12  
        if abs(altura_actual - altura_objetivo) > paso:
            nueva_altura = altura_actual + paso if altura_actual < altura_objetivo else altura_actual - paso
            self.ventana.geometry(f"450x{nueva_altura}")
            self.ventana.after(10, lambda: self.animar_ventana(altura_objetivo))
        else:
            self.ventana.geometry(f"450x{altura_objetivo}")

    def actionPerformed(self): 
        try:
            valores = [self.campoNota1.get(), self.campoNota2.get(), self.campoNota3.get(), self.campoNota4.get(), self.campoNota5.get()]
            
            for valor in valores:
                if valor.strip() == "":
                    raise CamposVaciosError("Los 5 campos son obligatorios. No dejes ninguno vacío.")
                    
            valores = [float(valor) for valor in valores]
            for valor in valores:
                if valor < 0 or valor > 5:
                    raise NotaFueraDeRangoError("Atención: Las notas deben estar en un rango de 0 a 5.")
                    
            self.notas = Notas(*valores) 
            notas = self.notas
            self.lbl_resultado.config(text=f"Promedio = {notas.calcularPromedio():.2f}")
            self.lbl_resultado2.config(text=f"Desviación estándar = {notas.calcularDesviacion():.2f}")
            self.lbl_resultado3.config(text=f"Valor mayor = {notas.calcularMayor():.2f}")
            self.lbl_resultado4.config(text=f"Valor menor = {notas.calcularMenor():.2f}")
            
            self.frame_resultados.pack(pady=15, fill="x", padx=30)
            self.animar_ventana(600)
                    
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Atención: Ingresa únicamente números.")
        except CamposVaciosError as error_vacio:
            messagebox.showwarning("Campos Incompletos", str(error_vacio))
        except NotaFueraDeRangoError as error_rango:
            messagebox.showwarning("Rango Inválido", str(error_rango))

    def limpiar(self):
        for entrada in self.entradas:
            entrada.delete(0, tk.END)
        self.frame_resultados.pack_forget()
        self.animar_ventana(390)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = VentanaPrincipal(raiz)
    raiz.mainloop()