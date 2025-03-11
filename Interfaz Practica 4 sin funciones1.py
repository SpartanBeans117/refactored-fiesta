import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Interfaz")

#Aqui se crea el area del texto
cuadrotexto = tk.Label(root, text="Area del texto:")
cuadrotexto.pack(pady=10)
area_texto = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
area_texto.pack(pady=10)

#Aqui se crea el menu
menu = tk.Menu(root)

menu_texto = tk.Menu(menu, tearoff=0)
menu_texto.add_command(label="Abrir", accelerator="Ctrl+A")
menu_texto.add_command(label="Guardar", accelerator="Ctrl+G")
menu_texto.add_command(label="Borrar", accelerator="Ctrl+B")
menu_texto.add_separator()
menu_texto.add_command(label="Salir", accelerator="Ctrl+Q", command=root.quit)
menu.add_cascade(label="Archivo", men=menu_texto)

root.config(men=menu)
    

#Se crea el boton buscar y remplazar
boton = tk.Button(root, text="Buscar y Remplazar", command=0)
boton.pack(pady=20)


#Se crea el boton cambiar color
boton = tk.Button(root, text="Cambiar Color", command=0)
boton.pack(pady=20)

#asignamos las funciones
menu_texto.entryconfig("Abrir", command=0)
menu_texto.entryconfig("Guardar", command=0)
menu_texto.entryconfig("Borrar", command=0)
menu_texto.entryconfig("Salir", command=0)

#Asignamos las teclas 
root.bind_all("<Control-a>", lambda event: ())
root.bind_all("<Control-g>", lambda event: ())
root.bind_all("<Control-b>", lambda event: ())
root.bind_all("<Control-q>", lambda event: ())


root.mainloop()
