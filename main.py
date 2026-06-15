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


def guardar_paises(nombre_archivo, paises):
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            escritor.writeheader()
            escritor.writerows(paises)

    except PermissionError:
        print("Error: no se pudo guardar el archivo. Verifique que no esté abierto.")


def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
    else:
        print("\nListado de países:")
        for pais in paises:
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")


def pedir_texto_no_vacio(mensaje):
    dato = input(mensaje)

    while dato.strip() == "":
        dato = input("El campo no puede estar vacío. Ingrese nuevamente: ")

    return dato.strip()


def pedir_entero_positivo(mensaje):
    numero = input(mensaje)

    while not numero.isdigit() or int(numero) <= 0:
        numero = input("Debe ingresar un número entero positivo: ")

    return int(numero)


def agregar_pais(paises):
    print("\nAgregar nuevo país")

    nombre = pedir_texto_no_vacio("Ingrese el nombre del país: ")
    poblacion = pedir_entero_positivo("Ingrese la población: ")
    superficie = pedir_entero_positivo("Ingrese la superficie en km²: ")
    continente = pedir_texto_no_vacio("Ingrese el continente: ")

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)
    guardar_paises("paises.csv", paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):
    print("\nActualizar datos de un país")

    nombre_buscado = pedir_texto_no_vacio("Ingrese el nombre exacto del país a actualizar: ")
    encontrado = False

    for pais in paises:
        if pais["nombre"] == nombre_buscado:
            print(f"País encontrado: {pais['nombre']}")
            print(f"Población actual: {pais['poblacion']}")
            print(f"Superficie actual: {pais['superficie']} km²")

            nueva_poblacion = pedir_entero_positivo("Ingrese la nueva población: ")
            nueva_superficie = pedir_entero_positivo("Ingrese la nueva superficie en km²: ")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            guardar_paises("paises.csv", paises)

            print("País actualizado correctamente.")
            encontrado = True

    if encontrado == False:
        print("No se encontró un país con ese nombre.")

def buscar_pais_por_nombre(paises):
    print("\nBuscar país por nombre")

    nombre_buscado = pedir_texto_no_vacio("Ingrese el nombre o parte del nombre del país: ")
    encontrados = []

    for pais in paises:
        if nombre_buscado in pais["nombre"]:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países con ese nombre.")
    else:
        print("\nResultados encontrados:")
        mostrar_paises(encontrados)

def filtrar_por_continente(paises):
    print("\nFiltrar países por continente")

    continente_buscado = pedir_texto_no_vacio("Ingrese el continente: ")
    encontrados = []

    for pais in paises:
        if pais["continente"] == continente_buscado:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países para ese continente.")
    else:
        mostrar_paises(encontrados)


def filtrar_por_rango_poblacion(paises):
    print("\nFiltrar países por rango de población")

    minimo = pedir_entero_positivo("Ingrese la población mínima: ")
    maximo = pedir_entero_positivo("Ingrese la población máxima: ")
    encontrados = []

    if minimo > maximo:
        print("El valor mínimo no puede ser mayor que el máximo.")
    else:
        for pais in paises:
            if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
                encontrados.append(pais)

        if len(encontrados) == 0:
            print("No se encontraron países en ese rango de población.")
        else:
            mostrar_paises(encontrados)


def filtrar_por_rango_superficie(paises):
    print("\nFiltrar países por rango de superficie")

    minimo = pedir_entero_positivo("Ingrese la superficie mínima: ")
    maximo = pedir_entero_positivo("Ingrese la superficie máxima: ")
    encontrados = []

    if minimo > maximo:
        print("El valor mínimo no puede ser mayor que el máximo.")
    else:
        for pais in paises:
            if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
                encontrados.append(pais)

        if len(encontrados) == 0:
            print("No se encontraron países en ese rango de superficie.")
        else:
            mostrar_paises(encontrados)


def filtrar_paises(paises):
    opcion = ""

    while opcion != "4":
        print("\n--- Filtros ---")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("4. Volver al menú principal")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            filtrar_por_continente(paises)

        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)

        elif opcion == "3":
            filtrar_por_rango_superficie(paises)

        elif opcion == "4":
            print("Volviendo al menú principal...")

        else:
            print("Opción inválida. Ingrese una opción del 1 al 4.")


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
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais_por_nombre(paises)

        elif opcion == "5":
            filtrar_paises(paises)
            
        elif opcion == "6":
            print("Funcionalidad pendiente: ordenar países.")

        elif opcion == "7":
            print("Funcionalidad pendiente: mostrar estadísticas.")

        elif opcion == "8":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida. Ingrese una opción del 1 al 8.")


ejecutar_programa()
