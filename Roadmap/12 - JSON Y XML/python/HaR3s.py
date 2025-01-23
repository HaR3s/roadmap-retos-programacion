#!/data/data/com.termux/files/usr/bin/python3

"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
*
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
* siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
* - Nombre
* - Edad
* - Fecha de nacimiento
* - Listado de lenguajes de programación
* Muestra el contenido de los archivos.
* Borra los archivos.
*
* DIFICULTAD EXTRA (opcional):
* Utilizando la lógica de creación de los archivos anteriores, crea un
* programa capaz de leer y transformar en una misma clase custom de tu
* lenguaje los datos almacenados en el XML y el JSON.
* Borra los archivos.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

import os
import json

data = {
    "name": "Zeidel Garcia",
    "age": 25,
    "birth_date": "27-08-1999",
    "programming_languages": ["Python", "Java", "C++"],
}

json_file = "HaR3s.json"


def make_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

    json_data.close()


make_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

    json_data.close()

os.remove("HaR3s.json")
