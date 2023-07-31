import os
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
import folium
import webbrowser
import json
from models import Evento, Ubicacion

class VentanaSecundaria(tk.Toplevel):
    def __init__(self, eventos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Índice de eventos")
        for evento in eventos:
            evento_label = tk.Label(self, text=f"Nombre: {evento.nombre}, Artista: {evento.artista}")
            evento_label.pack()

class VentanaPrincipal(tk.Tk):
    def __init__(self, eventos, ubicaciones, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")

        image_path = "/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/images/Salta_1.jpeg"
        if os.path.exists(image_path):
            self.background_image = Image.open(image_path)
            self.background_photo = ImageTk.PhotoImage(self.background_image)
        else:
            print("Error: No se encontró la imagen de fondo.")

        titulo_font = Font(family='Roboto', size=16, weight='bold')
        texto_font = Font(family='Open Sans', size=12)

        content_frame = tk.Frame(self)
        content_frame.place(x=0, y=0, relwidth=1, relheight=1)

        background_frame = tk.Frame(content_frame)
        background_frame.place(x=0, y=0, relwidth=1, relheight=1)

        titulo_label = tk.Label(content_frame, text='Tour Musical', font=titulo_font)
        titulo_label.pack(pady=20)

        indice_eventos_button = tk.Button(content_frame, text='Índice de Eventos', font=texto_font, command=lambda: self.mostrar_indice_eventos(eventos))
        indice_eventos_button.pack(pady=10)

        ubicacion_button = tk.Button(content_frame, text='Ubicación', font=texto_font, command=lambda: self.mostrar_ubicacion(ubicaciones))
        ubicacion_button.pack(pady=10)

        quit_button = tk.Button(content_frame, text='Quit', font=texto_font, command=self.quit)
        quit_button.pack(pady=10)

        if hasattr(self, 'background_photo'):
            self.background_label = tk.Label(background_frame, image=self.background_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        ancho = event.width
        alto = event.height
        background_image_resized = self.background_image.resize((ancho, alto), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(background_image_resized)
        self.background_label.config(image=self.background_photo)

    def mostrar_indice_eventos(self, eventos):
        self.ventana_secundaria = VentanaSecundaria(eventos)

    def mostrar_ubicacion(self, ubicaciones):
        mapa = folium.Map(location=[-24.7859, -65.41166], zoom_start=13)
        for ubicacion in ubicaciones:
            folium.Marker(location=ubicacion.coordenadas, popup=ubicacion.nombre).add_to(mapa)

        mapa.save("mapa_ubicaciones.html")
        webbrowser.open("mapa_ubicaciones.html")

if __name__ == "__main__":
    with open("eventos.json", "r") as file:
        eventos_json = json.load(file)
        eventos = [Evento(**evento) for evento in eventos_json]

    with open("ubicaciones.json", "r") as file:
        ubicaciones_json = json.load(file)
        ubicaciones = [Ubicacion(**ubicacion) for ubicacion in ubicaciones_json]

    root = VentanaPrincipal(eventos, ubicaciones)
    root.mainloop()

