from archivo_paises import leer_paises
from gestion_paises import mostrar_paises
from gestion_paises import agregar_pais
from gestion_paises import actualizar_pais
from gestion_paises import buscar_pais_por_nombre
from gestion_paises import filtrar_paises
from gestion_paises import ordenar_paises
from gestion_paises import mostrar_estadisticas


# Muestra el menú principal del sistema.
def mostrar_menu():
    print("\n--- Sistema de Gestión de Países ---")
    print("1. Mostrar países")
    print("2. Agregar país")
    print("3. Actualizar país")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Salir")


# Función principal del programa. Controla el menú y llama a las funciones correspondientes.
def ejecutar_programa():
    paises = leer_paises("paises.csv")
    opcion = ""

    while opcion != "8":
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais_por_nombre(paises)

        elif opcion == "5":
            filtrar_paises(paises)

        elif opcion == "6":
            ordenar_paises(paises)

        elif opcion == "7":
            mostrar_estadisticas(paises)

        elif opcion == "8":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida. Ingrese una opción del 1 al 8.")


# Llamada inicial para ejecutar el programa.
ejecutar_programa()
