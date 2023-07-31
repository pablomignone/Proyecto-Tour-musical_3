import json

def guardar_Evento(evento, archivo):
    with open(archivo, 'w') as file:
        json.dump(evento.__dict__, file, indent=4)

def cargar_eventos(archivo):
    try:
        with open(archivo, 'r') as file:
            eventos = json.load(file)
            eventos_obj = [Evento(**evento) for evento in eventos]
            return eventos_obj
    except FileNotFoundError:
        return []

def guardar_Ubicacion(ubicacion, archivo):
    with open(archivo, 'w') as file:
        json.dump(ubicacion.__dict__, file, indent=4)

def cargar_ubicaciones(archivo):
    try:
        with open(archivo, 'r') as file:
            ubicaciones = json.load(file)
            ubicaciones_obj = [Ubicacion(**ubicacion) for ubicacion in ubicaciones]
            return ubicaciones_obj
    except FileNotFoundError:
        return []

class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

#Crear Eventos
# Crear un evento para Alan Sutton y las criaturitas de la ansiedad
evento1 = Evento(
    id = 1,
    nombre = "Alan Sutton y las criaturitas de la ansiedad",
    artista = "Alan Sutton y las criaturitas de la ansiedad",
    genero = "Rock alternativo",
    id_ubicacion = 1,
    hora_inicio = "21:00",
    hora_fin = "23:00",
    descripcion = "Una noche de rock alternativo con la banda liderada por Alan Sutton, que presenta su nuevo disco 'La vida es un sueño'.",
    imagen = "alan_sutton.jpg"
)

# Crear un evento para El Cuarteto de Nos
evento2 = Evento(
    id = 2,
    nombre = "El Cuarteto de Nos",
    artista = "El Cuarteto de Nos",
    genero = "Rock",
    id_ubicacion = 2,
    hora_inicio = "20:00",
    hora_fin = "22:00",
    descripcion = "Disfruta del humor y la música de la banda uruguaya El Cuarteto de Nos, que llega a Salta con su gira 'Jueves'.",
    imagen = "el_cuarteto_de_nos.jpg"
)

# Crear un evento para Homer El Mero Mero
evento3 = Evento(
    id = 3,
    nombre = "Homer El Mero Mero",
    artista = "Homer El Mero Mero",
    genero = "Hip hop",
    id_ubicacion = 2,
    hora_inicio = "19:00",
    hora_fin = "21:00",
    descripcion = "No te pierdas el show de Homer El Mero Mero, el rapero argentino que está revolucionando la escena del hip hop con su flow y sus letras.",
    imagen = "homer_el_mero_mero.jpg"
)
evento4 = Evento(
    id = 4,
    nombre = "14º Festival La Troja Canta",
    artista = "Varios",
    genero = "Folclore",
    id_ubicacion = 3,
    hora_inicio = "18:00",
    hora_fin = "02:00",
    descripcion = "Un festival para celebrar la música y la cultura folclórica de Salta, con la participación de artistas locales e invitados especiales.",
    imagen = "la_troja_canta.jpg"
)

# Crear una ubicación para El teatrino
ubicacion1 = Ubicacion(
    id = 1,
    nombre = "El Teatrino",
    direccion = "Aniceto Latorre y Alvear",
    coordenadas = (-24.7909, -65.4117)
)

# Crear una ubicación para el Teatro Provincial de Salta
ubicacion2 = Ubicacion(
    id = 2,
    nombre = "Teatro Provincial de Salta",
    direccion = "Zuviría 70",
    coordenadas = (-24.7888, -65.4105)
)

ubicacion3 = Ubicacion(
    id = 3,
    nombre = "La Troja",
    direccion = "Paraje La Troja, Salta",
    coordenadas = (-24.7859, -65.41166))

eventos = [evento1, evento2, evento3, evento4]
ubicaciones = [ubicacion1, ubicacion2, ubicacion3]

#Guardar eventos en el archivo "eventos_json"
with open("eventos.json", "w") as file:
    eventos_json = [evento.__dict__ for evento in eventos]
    json.dump(eventos_json, file, indent=4)

# Guardar ubicaciones en el archivo "ubicaciones.json"
with open("ubicaciones.json", "w") as file:
    ubicaciones_json = [ubicacion.__dict__ for ubicacion in ubicaciones]
    json.dump(ubicaciones_json, file, indent=4)

