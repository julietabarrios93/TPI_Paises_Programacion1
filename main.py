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


paises = leer_paises("paises.csv")

print("Países cargados correctamente:")
for pais in paises:
    print(pais)
