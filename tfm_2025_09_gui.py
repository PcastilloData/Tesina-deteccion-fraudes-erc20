import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import numpy as np

# --- Cargar modelos ---
with open("mejores_modelos.pkl", "rb") as f:
    modelos = pickle.load(f)

# --- Features ---
features = [
    'num_transfers_capped_log', 'approx_holders_capped_log', 'top10_concentration_proxy_capped_log',
    'avg_transfers_per_day_capped_log', 'std_transfers_per_day_capped_log', 'active_days_capped_log',
    'age_days_capped_log', 'inactive_days_proxy_capped_log'
]

# --- Función de predicción ---
def predecir():
    try:
        # Obtener modelo
        modelo_nombre = modelo_combo.get()
        modelo = modelos[modelo_nombre]

        # Leer valores de entrada
        valores = []
        for e in entries:
            val = float(e.get())
            valores.append(val)
        X_input = np.array(valores).reshape(1, -1)

        # Predicción
        y_pred = modelo.predict(X_input)[0]
        if hasattr(modelo, "predict_proba"):
            prob = modelo.predict_proba(X_input).max()
        else:
            prob = None

        # Mostrar resultado
        resultado = f"Predicción: {y_pred}"
        if prob is not None:
            resultado += f" (Probabilidad: {prob:.2f})"
        messagebox.showinfo("Resultado", resultado)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI ---
root = tk.Tk()
root.title("Inferencia Modelos")

# Selección de modelo
tk.Label(root, text="Selecciona modelo:").grid(row=0, column=0, padx=5, pady=5)
modelo_combo = ttk.Combobox(root, values=list(modelos.keys()), state="readonly")
modelo_combo.grid(row=0, column=1, padx=5, pady=5)
modelo_combo.current(0)

# Entradas de features
entries = []
for i, feat in enumerate(features):
    tk.Label(root, text=feat).grid(row=i+1, column=0, padx=5, pady=2, sticky="e")
    e = tk.Entry(root)
    e.grid(row=i+1, column=1, padx=5, pady=2)
    entries.append(e)

# Botón de predicción
tk.Button(root, text="Predecir", command=predecir).grid(row=len(features)+1, column=0, columnspan=2, pady=10)

root.mainloop()






