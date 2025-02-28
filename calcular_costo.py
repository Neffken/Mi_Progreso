import tkinter as tk
from tkinter import messagebox

def calcular_precio():
    try:
        costo_filamento_kg = float(entry_filamento.get())
        gramos_usados = float(entry_gramos.get())
        consumo_impresora_w = float(entry_consumo.get())
        horas_impresion = float(entry_horas.get())
        costo_kwh = float(entry_kwh.get())
        margen_ganancia = float(entry_margen.get())
        
        costo_por_gramo = costo_filamento_kg / 1000
        costo_filamento = gramos_usados * costo_por_gramo
        
        consumo_kwh = (consumo_impresora_w / 1000) * horas_impresion
        costo_electricidad = consumo_kwh * costo_kwh
        
        costo_total = costo_filamento + costo_electricidad
        precio_final = costo_total * (1 + margen_ganancia)
        
        resultado = (f"Costo de filamento: {costo_filamento:.2f}\n"
                     f"Costo de electricidad: {costo_electricidad:.2f}\n"
                     f"Costo total: {costo_total:.2f}\n"
                     f"Precio sugerido: {precio_final:.2f}")
        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

root = tk.Tk()
root.title("Calculadora de Precio de Impresión 3D")

tk.Label(root, text="Costo del filamento por kilo:").grid(row=0, column=0)
entry_filamento = tk.Entry(root)
entry_filamento.grid(row=0, column=1)

tk.Label(root, text="Cantidad de filamento usado (g):").grid(row=1, column=0)
entry_gramos = tk.Entry(root)
entry_gramos.grid(row=1, column=1)

tk.Label(root, text="Consumo de la impresora (W):").grid(row=2, column=0)
entry_consumo = tk.Entry(root)
entry_consumo.grid(row=2, column=1)

tk.Label(root, text="Tiempo de impresión (horas):").grid(row=3, column=0)
entry_horas = tk.Entry(root)
entry_horas.grid(row=3, column=1)

tk.Label(root, text="Costo de la electricidad por kWh:").grid(row=4, column=0)
entry_kwh = tk.Entry(root)
entry_kwh.grid(row=4, column=1)

tk.Label(root, text="Margen de ganancia (ej. 1.5 para 50% extra):").grid(row=5, column=0)
entry_margen = tk.Entry(root)
entry_margen.grid(row=5, column=1)

tk.Button(root, text="Calcular Precio", command=calcular_precio).grid(row=6, columnspan=2)

root.mainloop()
