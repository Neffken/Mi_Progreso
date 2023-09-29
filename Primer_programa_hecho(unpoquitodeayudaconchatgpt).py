import tkinter as tk
from random import randint, choice

def asignar_numero(lista_numeros):
    numero = randint(1, 5)
    while numero in lista_numeros:
        numero = randint(1, 5)
    lista_numeros.append(numero)
    return numero

def realizar_sorteo():
    lista_nombres = []
    lista_numeros = []

    for _ in range(5):
        nombre = nombre_entries[_].get()
        rifa = asignar_numero(lista_numeros)
        comprador = f"Nombre: {nombre}, Rifa: {rifa}"
        lista_nombres.append(comprador)

    ganador = choice(lista_nombres)
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, f"Los participantes son:\n\n")
    for participante in lista_nombres:
        resultado_text.insert(tk.END, f"{participante}\n")
    resultado_text.insert(tk.END, f"\nEl ganador del sorteo es:\n\n{ganador}")

# Crear ventana de Tkinter
ventana = tk.Tk()
ventana.title("El lauti")

nombre_entries = []
for i in range(5):
    label = tk.Label(ventana, text=f"Nombre del comprador {i + 1}:")
    label.pack()
    entry = tk.Entry(ventana)
    entry.pack()
    nombre_entries.append(entry)

sorteo_button = tk.Button(ventana, text="Realizar Sorteo", command=realizar_sorteo)
sorteo_button.pack()

resultado_text = tk.Text(ventana, height=10, width=40)
resultado_text.pack()

ventana.mainloop()
