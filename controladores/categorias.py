from vistas.menu_consola import mostrar_menu_categoria, mostrar_elementos

def manejar_ver_categoria(coleccion):
    while True:
        mostrar_menu_categoria()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == '1':
            mostrar_elementos(coleccion['libros'], 'libros')
        elif opcion == '2':
            mostrar_elementos(coleccion['peliculas'], 'películas')
        elif opcion == '3':
            mostrar_elementos(coleccion['musica'], 'música')
        elif opcion == '4':
            return
        else:
            print("Opción no válida.")
