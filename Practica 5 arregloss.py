import os
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

root = tk.Tk()
root.title("Interfaz")

# Aquí se crea el area del texto
cuadrotexto = tk.Label(root, text="Cuadro de texto:")
cuadrotexto.pack(pady=10)
area_texto = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
area_texto.pack(pady=10)

# Aquí se crea el menu
menu = tk.Menu(root)

menu_texto = tk.Menu(menu, tearoff=0)
menu_texto.add_command(label="Abrir", accelerator="Ctrl+A")
menu_texto.add_command(label="Guardar", accelerator="Ctrl+G")
menu_texto.add_command(label="Editar", accelerator="Ctrl+E")
menu_texto.add_command(label="Borrar", accelerator="Ctrl+B")
menu_texto.add_separator()
menu_texto.add_command(label="Salir", accelerator="Ctrl+Q", command=root.quit)
menu.add_cascade(label="Archivo", menu=menu_texto)

root.config(menu=menu)

# Definicion de la clase FileManager
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def abrir_archivo(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "Archivo no encontrado."
        except IOError:
            return "Error al abrir el archivo."

    def guardar_archivo(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
                return "Archivo guardado exitosamente."
        except IOError:
            return "Error al guardar el archivo."

    def editar_archivo(self, new_content):
        try:
            with open(self.file_path, 'a') as file:
                file.write(new_content)
                return "Contenido añadido exitosamente."
        except IOError:
            return "Error al editar el archivo."

    def borrar_archivo(self):
        try:
            os.remove(self.file_path)
            return "Archivo eliminado exitosamente."
        except FileNotFoundError:
            return "Archivo no encontrado."
        except IOError:
            return "Error al eliminar el archivo."

# Aqui se le puede agregar las acciones/funciones
def abrir():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        file_manager = FileManager(file_path)
        content = file_manager.abrir_archivo()
        area_texto.delete(1.0, tk.END)
        area_texto.insert(tk.END, content)

def guardar():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        content = area_texto.get(1.0, tk.END)
        file_manager = FileManager(file_path)
        message = file_manager.guardar_archivo(content)
        messagebox.showinfo("Guardar archivo", message)

def borrar():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        file_manager = FileManager(file_path)
        message = file_manager.borrar_archivo()
        messagebox.showinfo("Eliminar archivo", message)

def editar():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        new_content = area_texto.get(1.0, tk.END)
        file_manager = FileManager(file_path)
        message = file_manager.editar_archivo(new_content)
        messagebox.showinfo("Editar archivo", message)

def salir():
    root.quit()

# Funcion buscar y reemplazar
def ByRemplazar():
    print("buscado y reemplazado")

# Se crea el boton buscar y reemplazar
boton_buscar_reemplazar = tk.Button(root, text="Buscar y Reemplazar", command=ByRemplazar)
boton_buscar_reemplazar.pack(pady=20)

# Funcion cambiar color del texto
def cambiarColor():
    print("color cambiado")

# Se crea el boton cambiar color
boton_cambiar_color = tk.Button(root, text="Cambiar Color", command=cambiarColor)
boton_cambiar_color.pack(pady=20)

# Asignamos las funciones
menu_texto.entryconfig("Abrir", command=abrir)
menu_texto.entryconfig("Guardar", command=guardar)
menu_texto.entryconfig("Editar", command=editar)
menu_texto.entryconfig("Borrar", command=borrar)
menu_texto.entryconfig("Salir", command=salir)

# Asignamos las teclas
root.bind_all("<Control-a>", lambda event: abrir())
root.bind_all("<Control-g>", lambda event: guardar())
root.bind_all("<Control-e>", lambda event: editar())
root.bind_all("<Control-b>", lambda event: borrar())
root.bind_all("<Control-q>", lambda event: salir())

root.mainloop()
