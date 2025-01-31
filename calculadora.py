import tkinter as tk
from tkinter import messagebox
import math

# Configuración de colores y fuentes
COLOR_FONDO = "#F0F0F0"  # Fondo claro
COLOR_BOTONES_NUMEROS = "#FFFFFF"  # Botones numéricos (blanco)
COLOR_BOTONES_OPERADORES = "#FFD700"  # Botones de operadores (dorado)
COLOR_BOTONES_ESPECIALES = "#FF6347"  # Botones especiales (rojo coral)
COLOR_TEXTO = "#000000"  # Texto negro
COLOR_PANTALLA = "#E0E0E0"  # Fondo de la pantalla (gris claro)
FUENTE = ("Comic Sans MS", 20, "bold")  # Fuente divertida y grande

# Función para mostrar mensajes de error con sugerencias
def mostrar_error(mensaje):
    sugerencia = "Sugerencias:\n"
    if "division by zero" in str(mensaje):
        sugerencia += "No puedes dividir entre cero. Intenta con otro número."
    elif "invalid literal for int()" in str(mensaje):
        sugerencia += "Asegúrate de ingresar números válidos."
    elif "math domain error" in str(mensaje):
        sugerencia += "No se puede calcular la raíz cuadrada de un número negativo."
    elif "could not convert string to float" in str(mensaje):
        sugerencia += "Ingresa solo números y operadores válidos."
    else:
        sugerencia += "Revisa la expresión ingresada. Asegúrate de que sea correcta."
    
    messagebox.showerror("Error", f"¡Ups! Algo salió mal.\n\n{sugerencia}")

# Función para actualizar la pantalla de la calculadora
def agregar_a_pantalla(valor):
    pantalla.insert(tk.END, valor)

# Función para calcular el resultado
def calcular():
    try:
        expresion = pantalla.get()
        expresion = expresion.replace('^', '**')  # Reemplazar '^' por '**' para potencias
        resultado = str(eval(expresion))
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

# Función para limpiar la pantalla
def limpiar_pantalla():
    pantalla.delete(0, tk.END)

# Funciones científicas
def calcular_seno():
    try:
        valor = float(pantalla.get())
        resultado = math.sin(math.radians(valor))  # Convierte a radianes
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_coseno():
    try:
        valor = float(pantalla.get())
        resultado = math.cos(math.radians(valor))  # Convierte a radianes
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_tangente():
    try:
        valor = float(pantalla.get())
        resultado = math.tan(math.radians(valor))  # Convierte a radianes
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_logaritmo():
    try:
        valor = float(pantalla.get())
        resultado = math.log10(valor)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_raiz_cuadrada():
    try:
        valor = float(pantalla.get())
        resultado = math.sqrt(valor)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_potencia():
    try:
        expresion = pantalla.get()
        base, exponente = expresion.split('^')
        resultado = math.pow(float(base), float(exponente))
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_factorial():
    try:
        valor = int(pantalla.get())
        resultado = math.factorial(valor)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_permutacion():
    try:
        n, r = map(int, pantalla.get().split('P'))
        resultado = math.perm(n, r)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_combinacion():
    try:
        n, r = map(int, pantalla.get().split('C'))
        resultado = math.comb(n, r)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

def calcular_porcentaje():
    try:
        valor = float(pantalla.get())
        resultado = valor / 100
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        mostrar_error(e)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora para Niños")
ventana.configure(bg=COLOR_FONDO)

# Crear la pantalla de la calculadora
pantalla = tk.Entry(ventana, font=("Comic Sans MS", 24), justify="right", bg=COLOR_PANTALLA, fg=COLOR_TEXTO, bd=10, relief=tk.FLAT)
pantalla.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=20)

# Definir los botones
botones = [
    '7', '8', '9', '/', 'C', '√',
    '4', '5', '6', '*', '^', 'sin',
    '1', '2', '3', '-', 'log', 'cos',
    '0', '.', '=', '+', 'nPr', 'tan',
    'nCr', '%', '!', '(', ')', 'π'
]

# Crear y colocar los botones en la ventana
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, font=FUENTE, bg=COLOR_BOTONES_ESPECIALES, fg=COLOR_TEXTO, bd=0, command=calcular).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)
    elif boton == 'C':
        tk.Button(ventana, text=boton, font=FUENTE, bg=COLOR_BOTONES_ESPECIALES, fg=COLOR_TEXTO, bd=0, command=limpiar_pantalla).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)
    elif boton in ['√', '^', 'sin', 'cos', 'tan', 'log', 'nPr', 'nCr', '!', '%', 'π']:
        tk.Button(ventana, text=boton, font=FUENTE, bg=COLOR_BOTONES_OPERADORES, fg=COLOR_TEXTO, bd=0, command=lambda b=boton: agregar_a_pantalla(b)).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)
    else:
        tk.Button(ventana, text=boton, font=FUENTE, bg=COLOR_BOTONES_NUMEROS, fg=COLOR_TEXTO, bd=0, command=lambda b=boton: agregar_a_pantalla(b)).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)
    columna += 1
    if columna > 5:
        columna = 0
        fila += 1

# Iniciar el bucle principal de la ventana
ventana.mainloop()