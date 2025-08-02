from vistas.menu_consola import mostrar_menu_listar, mostrar_elementos

def manejar_listar_elementos(coleccion):
    while True:
        mostrar_menu_listar()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            mostrar_elementos(coleccion['libros'], 'libros')
        elif opcion == '2':
            mostrar_elementos(coleccion['peliculas'], 'películas')
        elif opcion == '3':
            mostrar_elementos(coleccion['musica'], 'música')
        elif opcion == '4':
            elementos = coleccion['libros'] + coleccion['peliculas'] + coleccion['musica']
            mostrar_elementos(elementos)
        elif opcion == '5':
            return
        else:
            print("Opción no válida.")
