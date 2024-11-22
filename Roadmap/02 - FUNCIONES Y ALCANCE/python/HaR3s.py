#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* - Crea ejemplos de funciones básicas que representen las diferentes
*   posibilidades del lenguaje:
*   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
* - Comprueba si puedes crear funciones dentro de funciones.
* - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
* - Pon a prueba el concepto de variable LOCAL y GLOBAL.
* - Debes hacer print por consola del resultado de todos los ejemplos.
*   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
*
* DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*
* Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
* Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

global_var = 10


def psaludo():  # definicion de funcion sin parametros ni retorno
    print("Hola Mundo")


def rsaludo():  # funcion que no recibe parametros pero tiene retorno
    return global_var


def saludo(txt: str) -> str:  # funcion con parametro y retorno
    return txt


def sumar(a, b):  # funcion que recibe dos parametros pero nondevuelve nada
    local_var = a + b
    print(f"{global_var} + {local_var} = {global_var + local_var}")


def funcionSuperior():
    def funcionInferior():  # funcion dentro de otra
        print("Hola Mundo")

    funcionInferior()


def multiParam(*args):  # funcion con multiples parametros
    return sum(args)


def multiParamCV(
    **kwargs,
):  # funcion que recibe parametros Clave Valor y retorna un diccionario
    return kwargs


def multiOperacion(a, b):  # funcion que retorna dos valores
    return a + b, a - b


# EJERCICIO OPCIONAL
def opcional(string1: str, string2: str):
    cont = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(string1, "", string2)
        elif i % 3 == 0:
            print(string1)
        elif i % 5 == 0:
            print(string2)
        else:
            print(i)
            cont += 1
    return cont


if __name__ == "__main__":
    psaludo()
    print(rsaludo())  # uso de funcion predeterminada de python
    print(saludo("Hola a todos"))
    sumar(50, 5)
    funcionSuperior()
    print(multiParam(10, 20, 50, 29, 45))
    print(multiParamCV(uno=1, dos=2, tres=3, cuatro=4, cinco=5))
    suma, resta = multiOperacion(10, 5)
    print(suma, "", resta)
    print(multiOperacion(10, 5))
    cont = opcional("Hola", "Mundo")
    print(f"Entre 1 y 100 hay {cont} # que no son multiplos de 3, 5 o ambos")
