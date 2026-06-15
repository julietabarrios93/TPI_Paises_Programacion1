import csv


# Lee los países desde el archivo CSV y los guarda en una lista de diccionarios.
def leer_paises(nombre_archivo):
    paises = []

    try:
        # Se abre el archivo en modo lectura usando UTF-8 para admitir tildes y caracteres especiales.
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Cada fila del CSV se transforma en un diccionario.
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


# Guarda la lista de países en el archivo CSV, manteniendo los encabezados.
def guardar_paises(nombre_archivo, paises):
    try:
        # newline="" evita líneas en blanco extra al escribir archivos CSV.
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            escritor.writeheader()
            escritor.writerows(paises)

    except PermissionError:
        print("Error: no se pudo guardar el archivo. Verifique que no esté abierto.")
