import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("Aplicación ventana")

ventana.configure(bg="lightgreen")

etiqueta = tk.Label(ventana, text="Bienvenido", bg="lightgreen")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

def mostrar_contenido():
    contenido = entrada.get()
    messagebox.showinfo("Contenido del cuadro de texto", contenido)

boton_mostrar = tk.Button(ventana, text="Mostrar contenido", command=mostrar_contenido)
boton_mostrar.pack(pady=10)

boton_cerrar = tk.Button(ventana, text="Cerrar aplicación", command=ventana.quit)
boton_cerrar.pack(pady=10)

ventana.mainloop()
