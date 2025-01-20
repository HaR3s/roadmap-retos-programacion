#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
* implemente una superclase Animal y un par de subclases Perro y Gato,
* junto con una función que sirva para imprimir el sonido que emite cada Animal.
*
* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"


class Animal:
    def __init__(self, patas: int, pelo: bool) -> None:
        self.patas = patas
        self.pelo = pelo


class Perro(Animal):
    def __init__(self) -> None:
        super().__init__(4, True)
        self.raza = "Perro"
        self.sonido = "ladrar"

    def __str__(self) -> str:
        return f"raza: {self.raza}, sonido: {self.sonido}, patas: {self.patas}, pelo: {self.pelo}"


class Gato(Animal):
    def __init__(self) -> None:
        super().__init__(4, True)
        self.raza = "Gato"
        self.sonido = "maullar"

    def __str__(self) -> str:
        return f"raza: {self.raza}, sonido: {self.sonido}, patas: {self.patas}, pelo: {self.pelo}"


perro = Perro()
gato = Gato()

print(str(perro))
print(str(gato))


class Empleados:
    def __init__(self, cargo: str | None, id: int | None, nombre: str | None):
        self.nombre = nombre
        self.cargo = cargo
        self.id = id

    def getID(self):
        return self.id

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, ID: {self.id}, "


class Gerentes(Empleados):
    def __init__(self, nombre: str | None, id):
        super().__init__("Gerente", id, nombre)
        self.funciones = "Director General"

    def __str__(self) -> str:
        return super().__str__() + self.funciones


class GerentesGenerales(Empleados):
    def __init__(self, nombre: str | None, id):
        super().__init__("Gerente general", id, nombre)
        self.funciones = "Director General de projectos"

    def __str__(self) -> str:
        return super().__str__() + self.funciones


class Programadores(Empleados):
    def __init__(self, nombre: str | None, id: int):
        super().__init__("programador", id, nombre)
        self.funciones = "Desarrollador de softwhare"

    def __str__(self) -> str:
        return super().__str__() + self.funciones


gerente1 = Gerentes("Miguel", 1)
gerente2 = Gerentes("Antonio", 2)

gerenteG = GerentesGenerales("Ana", 1)

progmm = Programadores("Alberto", 1)
progmm1 = Programadores("Alberto", 2)
progmm2 = Programadores("Alberto", 3)

print(str(gerente1))
print(str(gerente2))

print(str(gerenteG))

print(str(progmm))
print(str(progmm1))
print(str(progmm2))
