#importo librerias para crear ventana
import tkinter as tk
from tkinter import messagebox

#hago funciones
def suma(a, b):
    return a + b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return float(a / b)

def resultado():
    #el get sirve para obtener datos ingresados por la persona ej: casi igual a "input"
    a = float(cuandro_numero1.get())
    b = float(cuandro_numero2.get())

    resultado_sum = suma(a,b)
    resultado_multiplicacion = multiplicacion(a,b)
    resultado_division = division(a,b)

    #mostrar resultados 
    messagebox.showinfo("Resultados", f"Suma: {resultado_sum}\nMultiplicación: {resultado_multiplicacion}\nDivisión: {resultado_division}")


# crear ventana principal

ventana = tk.Tk()
ventana.title("Calculadora de lauti")

#elijo resolucion de ventana
ventana.geometry("400x300")

#para hacer un espacio para ingresar numero
numero_1 = tk.Label(ventana, text="Ingresa numero")
numero_1.pack()

cuandro_numero1 = tk.Entry(ventana)
cuandro_numero1.pack()
#lo mismo que lo anterior
numero_2 = tk.Label(ventana, text="Ingrese numero 2")
numero_2.pack()

cuandro_numero2 = tk.Entry(ventana)
cuandro_numero2.pack()

#crear el boton para calcular
boton_calcular = tk.Button(ventana, text="calcula", command=resultado)
boton_calcular.pack()

#para que se mantenga la ventana abierta
ventana.mainloop()
