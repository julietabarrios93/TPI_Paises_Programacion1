import csv


def leer_paises(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")

    except ValueError:
        print("Error: hay datos numéricos con formato incorrecto en el CSV.")

    return paises


def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
    else:
        print("\nListado de países:")
        for pais in paises:
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")


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


def ejecutar_programa():
    paises = leer_paises("paises.csv")
    opcion = ""

    while opcion != "8":
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            print("Funcionalidad pendiente: agregar país.")

        elif opcion == "3":
            print("Funcionalidad pendiente: actualizar país.")

        elif opcion == "4":
            print("Funcionalidad pendiente: buscar país.")

        elif opcion == "5":
            print("Funcionalidad pendiente: filtrar países.")

        elif opcion == "6":
            print("Funcionalidad pendiente: ordenar países.")

        elif opcion == "7":
            print("Funcionalidad pendiente: mostrar estadísticas.")

        elif opcion == "8":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida. Ingrese una opción del 1 al 8.")


ejecutar_programa()
