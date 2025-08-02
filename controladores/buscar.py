from vistas.menu_consola import mostrar_menu_buscar, mostrar_elementos

def manejar_buscar_elemento(coleccion):
    while True:
        mostrar_menu_buscar()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            criterio = 'titulo'
        elif opcion == '2':
            criterio = input("Buscar por (autor/director/artista): ").strip().lower()
        elif opcion == '3':
            criterio = 'genero'
        elif opcion == '4':
            return
        else:
            print("Opción no válida.")
            continue

        valor = input(f"Ingrese el {criterio} a buscar: ").strip()
        resultados = []
        for categoria in coleccion.values():
            for elemento in categoria:
                if valor.lower() in str(elemento.get(criterio, '')).lower():
                    resultados.append(elemento)
        mostrar_elementos(resultados, f"resultados de búsqueda por {criterio}")
