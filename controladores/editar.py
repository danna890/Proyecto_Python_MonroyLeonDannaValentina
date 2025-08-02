from vistas.menu_consola import mostrar_menu_editar, mostrar_menu_agregar, mostrar_elementos
from data.almacenamiento import guardar_coleccion

def manejar_editar_elemento(coleccion):
    print("\nSeleccione el tipo de elemento a editar:")
    mostrar_menu_agregar()
    opcion_tipo = input("Selecciona una opción (1-4): ").strip()
    if opcion_tipo == '4':
        return

    tipo = 'libros' if opcion_tipo == '1' else 'peliculas' if opcion_tipo == '2' else 'musica'

    elementos = coleccion[tipo]
    if not elementos:
        print(f"No hay {tipo} en la colección.")
        return

    mostrar_elementos(elementos, tipo)
    try:
        indice = int(input("Ingrese el número del elemento a editar: ")) - 1
        if indice < 0 or indice >= len(elementos):
            print("Número de elemento inválido.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    while True:
        mostrar_menu_editar()
        opcion_campo = input("Selecciona una opción (1-5): ").strip()
        if opcion_campo == '1':
            campo = 'titulo'
        elif opcion_campo == '2':
            campo = 'autor' if tipo == 'libros' else 'director' if tipo == 'peliculas' else 'artista'
        elif opcion_campo == '3':
            campo = 'genero'
        elif opcion_campo == '4':
            campo = 'valoracion'
        elif opcion_campo == '5':
            return
        else:
            print("Opción no válida.")
            continue

        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ").strip()
        elementos[indice][campo] = nuevo_valor
        guardar_coleccion(coleccion)
        print("¡Elemento actualizado correctamente!")
        return
