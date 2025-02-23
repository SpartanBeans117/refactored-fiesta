import tkinter as tk

def mostrar_evento(evento):
    etiqueta.config(text=f"Evento: {evento.type} - {evento.keysym if evento.type == 'KeyPress' else 'Mouse'}")

def cambiar_color(evento):
    ventana.config(bg="lightgreen")

def limpiar_texto(evento):
    etiqueta.config(text="")

ventana = tk.Tk()
ventana.title("Manejo de eventos")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Presiona teclas o haz clic", font=("Arial", 14))
etiqueta.pack(pady=20)

ventana.bind("<Button-1>", mostrar_evento)
ventana.bind("<Motion>", mostrar_evento)
ventana.bind("<Double-1>", cambiar_color)

ventana.bind("<KeyPress>", mostrar_evento)
ventana.bind("<space>", limpiar_texto)

ventana.mainloop()
