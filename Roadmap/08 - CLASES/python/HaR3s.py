#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
* atributos y una función que los imprima (teniendo en cuenta las posibilidades
* de tu lenguaje).
* Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
* utilizando su función.
*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"


class Ejemplo:
    def __init__(self, nombre: str | None, edad: int | None):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


ejm = Ejemplo("Zeidel", 25)

print(str(ejm))


# EXTRA


class Pila:
    def __init__(self, *arg):
        if arg is not None:
            self.lista = [i for i in arg]
        else:
            self.lista = []

    def __str__(self) -> str:
        return f"{self.lista[:]}"

    def dell(self):
        self.lista.pop()

    def add(self, element):
        self.lista.append(element)

    def __len__(self):
        return len(self.lista)


class Cola(Pila):
    def dell(self):
        self.lista.pop(0)


cola = Cola("Hola", 5839, False, 82883, "string")

pila = Pila(False, 82883, "string", 73738, True, "Hola")

print("Cola", len(cola))
print("Pila", len(pila))

print(str(cola))
print(str(pila))

cola.dell()

cola.add("Mundo")

print(str(cola))


pila.dell()

pila.add("Mundo")

print(str(pila))
