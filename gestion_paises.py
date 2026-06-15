from archivo_paises import guardar_paises


# Muestra por pantalla todos los países recibidos como parámetro.
def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
    else:
        print("\nListado de países:")
        for pais in paises:
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")


# Solicita un texto y valida que no esté vacío.
def pedir_texto_no_vacio(mensaje):
    dato = input(mensaje)

    while dato.strip() == "":
        dato = input("El campo no puede estar vacío. Ingrese nuevamente: ")

    return dato.strip()


# Solicita un número entero positivo y valida que el dato ingresado sea correcto.
def pedir_entero_positivo(mensaje):
    numero = input(mensaje)

    while not numero.isdigit() or int(numero) <= 0:
        numero = input("Debe ingresar un número entero positivo: ")

    return int(numero)


# Permite agregar un nuevo país a la lista y luego guarda los cambios en el CSV.
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


# Busca un país por nombre exacto y permite actualizar su población y superficie.
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


# Busca países por coincidencia exacta o parcial dentro del nombre.
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


# Filtra países cuyo continente coincida exactamente con el ingresado.
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


# Filtra países que tengan una población dentro del rango indicado.
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


# Filtra países que tengan una superficie dentro del rango indicado.
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


# Muestra un submenú para elegir el tipo de filtro.
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


# Crea una copia de la lista de países para ordenar sin modificar la lista original.
def copiar_lista_paises(paises):
    copia = []

    for pais in paises:
        copia.append(pais)

    return copia


# Ordena la lista de países usando Bubble Sort mejorado.
def ordenar_lista_paises(paises, campo, descendente):
    paises_ordenados = copiar_lista_paises(paises)
    n = len(paises_ordenados)

    for i in range(n - 1):
        hubo_intercambio = False

        for j in range(0, n - 1 - i):
            if descendente == False:
                if paises_ordenados[j][campo] > paises_ordenados[j + 1][campo]:
                    auxiliar = paises_ordenados[j]
                    paises_ordenados[j] = paises_ordenados[j + 1]
                    paises_ordenados[j + 1] = auxiliar
                    hubo_intercambio = True
            else:
                if paises_ordenados[j][campo] < paises_ordenados[j + 1][campo]:
                    auxiliar = paises_ordenados[j]
                    paises_ordenados[j] = paises_ordenados[j + 1]
                    paises_ordenados[j + 1] = auxiliar
                    hubo_intercambio = True

        # Si no hubo intercambios, la lista ya está ordenada.
        if hubo_intercambio == False:
            break

    return paises_ordenados


# Muestra un submenú para ordenar por nombre, población o superficie.
def ordenar_paises(paises):
    opcion = ""

    while opcion != "4":
        print("\n--- Ordenar países ---")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("4. Volver al menú principal")

        opcion = input("Ingrese una opción: ")

        if opcion == "1" or opcion == "2" or opcion == "3":
            print("\nTipo de orden:")
            print("1. Ascendente")
            print("2. Descendente")

            tipo_orden = input("Ingrese una opción: ")

            if opcion == "1":
                campo = "nombre"
            elif opcion == "2":
                campo = "poblacion"
            else:
                campo = "superficie"

            if tipo_orden == "1":
                paises_ordenados = ordenar_lista_paises(paises, campo, False)
                mostrar_paises(paises_ordenados)

            elif tipo_orden == "2":
                paises_ordenados = ordenar_lista_paises(paises, campo, True)
                mostrar_paises(paises_ordenados)

            else:
                print("Opción inválida. Ingrese 1 o 2.")

        elif opcion == "4":
            print("Volviendo al menú principal...")

        else:
            print("Opción inválida. Ingrese una opción del 1 al 4.")


# Calcula y muestra estadísticas generales del dataset de países.
def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
    else:
        pais_mayor_poblacion = paises[0]
        pais_menor_poblacion = paises[0]
        suma_poblacion = 0
        suma_superficie = 0
        continentes = {}

        for pais in paises:
            if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
                pais_mayor_poblacion = pais

            if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
                pais_menor_poblacion = pais

            suma_poblacion = suma_poblacion + pais["poblacion"]
            suma_superficie = suma_superficie + pais["superficie"]

            # Se cuenta cuántos países hay por cada continente.
            continente = pais["continente"]

            if continente in continentes:
                continentes[continente] = continentes[continente] + 1
            else:
                continentes[continente] = 1

        promedio_poblacion = suma_poblacion / len(paises)
        promedio_superficie = suma_superficie / len(paises)

        print("\n--- Estadísticas del dataset ---")
        print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
        print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
        print(f"Promedio de población: {promedio_poblacion:.2f}")
        print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

        print("\nCantidad de países por continente:")
        for continente in continentes:
            print(f"{continente}: {continentes[continente]}")
