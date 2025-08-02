from vistas.menu_consola import mostrar_menu_eliminar, mostrar_elementos
from data.almacenamiento import guardar_coleccion

def manejar_eliminar_elemento(coleccion):
    while True:
        mostrar_menu_eliminar()
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == '1':
            tipo = input("Ingrese el tipo (libros/peliculas/musica): ").strip()
            if tipo not in coleccion:
                print("Tipo no válido.")
                continue

            titulo = input("Ingrese el título del elemento a eliminar: ").strip()
            indice = next((i for i, e in enumerate(coleccion[tipo]) if e['titulo'].lower() == titulo.lower()), None)

            if indice is not None:
                elemento = coleccion[tipo][indice]
                confirmar = input(f"¿Está seguro de eliminar '{elemento['titulo']}'? (Si/No): ").lower()
                if confirmar == 'si':
                    coleccion[tipo].pop(indice)
                    guardar_coleccion(coleccion)
                    print("Elemento eliminado correctamente.")
            else:
                print("No se encontró el elemento con ese título.")

        elif opcion == '2':
            tipo = input("Ingrese el tipo (libros/peliculas/musica): ").strip()
            if tipo not in coleccion:
                print("Tipo no válido.")
                continue

            mostrar_elementos(coleccion[tipo], tipo)
            try:
                indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
                if 0 <= indice < len(coleccion[tipo]):
                    elemento = coleccion[tipo][indice]
                    confirmar = input(f"¿Está seguro de eliminar '{elemento['titulo']}'? (Si/No): ").lower()
                    if confirmar == 'si':
                        coleccion[tipo].pop(indice)
                        guardar_coleccion(coleccion)
                        print("Elemento eliminado correctamente.")
            except ValueError:
                print("Debe ingresar un número válido.")
        elif opcion == '3':
            return
        else:
            print("Opción no válida.")
