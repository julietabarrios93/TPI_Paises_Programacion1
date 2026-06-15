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
