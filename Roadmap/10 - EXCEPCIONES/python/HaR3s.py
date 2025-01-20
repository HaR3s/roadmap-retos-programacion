#!/data/data/com.termux/files/usr/bin/python3

"""
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
*
* DIFICULTAD EXTRA (opcional):
* Crea una función que sea capaz de procesar parámetros, pero que también
* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
* corresponderse con un tipo de excepción creada por nosotros de manera
* personalizada, y debe ser lanzada de manera manual) en caso de error.
* - Captura todas las excepciones desde el lugar donde llamas a la función.
* - Imprime el tipo de error.
* - Imprime si no se ha producido ningún error.
* - Imprime que la ejecución ha finalizado.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"


def dividir(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError()
    elif type(a) is str or type(b) is str:
        raise TypeError()
    else:
        return a / b


try:
    print(dividir(5, 0))
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

try:
    print(dividir(5, "nwkw"))
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

try:
    print(dividir(5, 3))
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
else:
    print("No se ha producido ningún error.")
finally:
    print("Ejecicion satisfactoria.")
