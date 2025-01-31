#!/data/data/com.termux/files/usr/bin/python3

"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
*
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo que se llame como
* tu usuario de GitHub y tenga la extensión .txt.
* Añade varias líneas en ese fichero:
* - Tu nombre.
* - Edad.
* - Lenguaje de programación favorito.
* Imprime el contenido.
* Borra el fichero.
*
* DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un
* archivo .txt.
* - Cada producto se guarda en una línea del archivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

import os

file_name = "HaRes.txt"

with open(file_name, "w") as file:
    file.write("Zeidel Garcia\n")
    file.write("25\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

file.close()

os.remove(file_name)

# EXTRA

file_name = "productos.txt"

open(file_name, "a")

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{nombre}, {cantidad}, {precio}\n")
    elif option == "2":
        nombre = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == nombre:
                    print(line)
                    break
    elif option == "3":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == nombre:
                    file.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    file.write(line)
    elif option == "4":
        nombre = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != nombre:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                componentes = line.split(", ")
                cantidad = int(componentes[1])
                precio = float(componentes[2])
                total += cantidad * precio
        print(total)
    elif option == "7":
        nombre = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == nombre:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Selecciona una opcion.")

file.close()
