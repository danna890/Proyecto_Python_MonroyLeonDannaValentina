from data.almacenamiento import cargar_coleccion, guardar_coleccion
from controladores.agregar import manejar_agregar_elemento
from controladores.listar import manejar_listar_elementos
from controladores.buscar import manejar_buscar_elemento
from controladores.editar import manejar_editar_elemento
from controladores.eliminar import manejar_eliminar_elemento
from controladores.categorias import manejar_ver_categoria
from vistas.menu_consola import mostrar_menu_principal

def main():
    coleccion = cargar_coleccion()

    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-8): ").strip()
        if opcion == '1':
            manejar_agregar_elemento(coleccion)
        elif opcion == '2':
            manejar_listar_elementos(coleccion)
        elif opcion == '3':
            manejar_buscar_elemento(coleccion)
        elif opcion == '4':
            manejar_editar_elemento(coleccion)
        elif opcion == '5':
            manejar_eliminar_elemento(coleccion)
        elif opcion == '6':
            manejar_ver_categoria(coleccion)
        elif opcion == '7':
            guardar_coleccion(coleccion)
            print("Colección guardada correctamente.")
        elif opcion == '8':
            guardar_coleccion(coleccion)
            print("¡Gracias por usar el Administrador de Colección!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

if __name__ == "__main__":
    main()
