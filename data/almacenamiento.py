import json
import os

RUTAS = {
    "libros": "libros.json",
    "peliculas": "peliculas.json",
    "musica": "musica.json"
}

def cargar_categoria(tipo: str):
    archivo = RUTAS.get(tipo)
    if archivo and os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    return []

def guardar_categoria(tipo: str, datos: list):
    archivo = RUTAS.get(tipo)
    with open(archivo, 'w') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_coleccion():
    return {
        "libros": cargar_categoria("libros"),
        "peliculas": cargar_categoria("peliculas"),
        "musica": cargar_categoria("musica")
    }

def guardar_coleccion(coleccion):
    for tipo, elementos in coleccion.items():
        guardar_categoria(tipo, elementos)
