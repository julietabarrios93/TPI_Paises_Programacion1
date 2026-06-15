# Sistema de Gestión de Países

Trabajo Práctico Integrador de la materia **Programación I**.

El proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar información de países almacenada en un archivo CSV. El sistema trabaja con datos como nombre, población, superficie y continente.

## Integrantes

* Nair Julieta Barrios
* Máximo Rossini

## Objetivo del proyecto

El objetivo del sistema es aplicar los contenidos vistos durante la materia Programación I, utilizando estructuras de datos, funciones, archivos CSV, validaciones, manejo de errores y modularización del código.

## Funcionalidades principales

El sistema permite:

* Mostrar el listado completo de países.
* Agregar un nuevo país al archivo CSV.
* Actualizar la población y superficie de un país existente.
* Buscar países por nombre exacto o parcial.
* Filtrar países por continente.
* Filtrar países por rango de población.
* Filtrar países por rango de superficie.
* Ordenar países por nombre, población o superficie.
* Mostrar estadísticas generales del dataset.

## Estadísticas disponibles

El sistema calcula y muestra:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

## Tecnologías utilizadas

* Python 3
* Archivos CSV
* Módulo `csv`
* Git y GitHub

## Estructura del proyecto

```text
tpi_paises/
├── main.py
├── archivo_paises.py
├── gestion_paises.py
├── paises.csv
└── README.md
```

## Descripción de los archivos

### `main.py`

Es el archivo principal del programa. Contiene el menú del sistema y controla la ejecución general de la aplicación.

### `archivo_paises.py`

Contiene las funciones encargadas de leer y guardar la información de los países en el archivo CSV.

### `gestion_paises.py`

Contiene las funciones relacionadas con la gestión de los países, como agregar, actualizar, buscar, filtrar, ordenar y calcular estadísticas.

### `paises.csv`

Es el archivo donde se almacena la información de los países. Cada país contiene los siguientes datos:

```text
nombre,poblacion,superficie,continente
```

## Ejemplo de datos del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Brasil,213993437,8515767,América
España,47450795,505990,Europa
China,1412000000,9596961,Asia
```

## Cómo ejecutar el programa

Para ejecutar el sistema, se debe abrir una terminal en la carpeta del proyecto y escribir:

```bash
python main.py
```

En algunos sistemas también puede ejecutarse con:

```bash
py main.py
```

## Menú principal

Al iniciar el programa, se muestra el siguiente menú:

```text
--- Sistema de Gestión de Países ---
1. Mostrar países
2. Agregar país
3. Actualizar país
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
8. Salir
```

## Validaciones implementadas

El programa valida que:

* Los campos de texto no estén vacíos.
* La población y la superficie sean números enteros positivos.
* Los rangos ingresados sean correctos.
* El archivo CSV exista antes de intentar leerlo.
* Los datos numéricos del CSV tengan un formato válido.
* El archivo CSV pueda guardarse correctamente.

## Modularización

El proyecto fue dividido en diferentes archivos para mejorar la organización del código.

Cada archivo tiene una responsabilidad específica:

```text
main.py → interacción con el usuario y menú principal
archivo_paises.py → lectura y escritura del archivo CSV
gestion_paises.py → lógica de gestión de países
```

Esta separación permite que el código sea más claro, ordenado y fácil de mantener.

## Conceptos aplicados

En el desarrollo del proyecto se aplicaron los siguientes contenidos de Programación I:

* Variables
* Condicionales
* Ciclos `while` y `for`
* Listas
* Diccionarios
* Funciones
* Parámetros
* Archivos CSV
* Manejo de errores con `try` y `except`
* Modularización
* Algoritmos de ordenamiento

## Ordenamiento

Para ordenar los países se utilizó el algoritmo **Bubble Sort mejorado**, permitiendo ordenar por:

* Nombre
* Población
* Superficie

El ordenamiento puede realizarse de forma ascendente o descendente.

## Estado del proyecto

Proyecto finalizado y funcional.
