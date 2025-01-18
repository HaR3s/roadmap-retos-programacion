#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* Entiende el concepto de recursividad creando una función recursiva que imprima
* números del 100 al 0.
*
* DIFICULTAD EXTRA (opcional):
* Utiliza el concepto de recursividad para:
* - Calcular el factorial de un número concreto (la función recibe ese número).
* - Calcular el valor de un elemento concreto (según su posición) en la
*   sucesión de Fibonacci (la función recibe la posición).
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"


def restaRecurciva(r):
    if r > 0:
        print(r)
        restaRecurciva(r - 1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def Fibonacci(n):
    if n <= 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


restaRecurciva(100)

print(factorial(5))

print(Fibonacci(5))
