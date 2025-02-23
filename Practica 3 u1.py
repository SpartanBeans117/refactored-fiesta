import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def validar_entrada():
    nombre = entry_nombre.get().strip()
    correo = entry_correo.get().strip()
    edad = entry_edad.get().strip()
    escolaridad = combo_escolaridad.get()

    if not nombre:
        messagebox.showerror("Error", "El campo de nombre no puede estar vacío.")
        return False

    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        messagebox.showerror("Error", "El formato del correo no es válido.")
        return False

    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return False

    return True

def enviar():
    if validar_entrada():
        messagebox.showinfo("Éxito", "Formulario enviado correctamente.")

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    combo_escolaridad.set("")

root = tk.Tk()
root.title("Formulario")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
entry_nombre = ttk.Entry(frame)
entry_nombre.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Correo:").grid(row=1, column=0, sticky=tk.W)
entry_correo = ttk.Entry(frame)
entry_correo.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Edad:").grid(row=2, column=0, sticky=tk.W)
entry_edad = ttk.Entry(frame)
entry_edad.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Escolaridad máxima:").grid(row=3, column=0, sticky=tk.W)
combo_escolaridad = ttk.Combobox(frame, values=["Primaria", "Secundaria", "Preparatoria", "Universidad"])
combo_escolaridad.grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Enviar", command=enviar).grid(row=4, column=0, sticky=tk.W)
ttk.Button(frame, text="Limpiar", command=limpiar).grid(row=4, column=1, sticky=tk.E)

root.mainloop()
