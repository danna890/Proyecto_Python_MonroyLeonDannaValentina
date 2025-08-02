from vistas.menu_consola import obtener_datos_elemento, mostrar_menu_agregar
from data.almacenamiento import guardar_coleccion

def manejar_agregar_elemento(coleccion):
    while True:
        mostrar_menu_agregar()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            tipo = 'libros'
        elif opcion == '2':
            tipo = 'peliculas'
        elif opcion == '3':
            tipo = 'musica'
        elif opcion == '4':
            return
        else:
            print("Opción no válida.")
            continue

        elemento = obtener_datos_elemento(tipo[:-1])
        coleccion[tipo].append(elemento)
        guardar_coleccion(coleccion)
        print(f"\n¡{elemento['titulo']} ha sido agregado a la colección de {tipo}!")
