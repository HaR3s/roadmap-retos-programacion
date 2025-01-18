#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"


# En python no existe el uso de valor y referencias pero este comportamiento
# se puede simular realizando copias de las variables y reasignando su valor


def parameterPerValue(x):
    return x * 2


ejemp1 = 20

print(ejemp1)
print(parameterPerValue(ejemp1))
print(ejemp1)

# El valor de la variable no se ve afectado

ejemp2 = [20, 30, 40]


def parameterPerRefer(x: list):
    x.append(50)


print(ejemp2)
parameterPerRefer(ejemp2)
print(ejemp2)

# De no querer que la lista original se vea afectada est se debe copiar a la funciom por medio de slicimg

parameterPerRefer(ejemp2[:])
print(ejemp2)


# EXTRA


def extra1(a, b):
    c = a
    a = b
    b = c
    return a * 2, b * 2


def extra2(list1: list, list2: list):
    list3 = list1
    list1 = list2
    list2 = list3
    return list1, list2


a, b = 10, 20

list1 = [1, 20, 30]
list2 = [10, 40, 60]

print(a)
print(b)

c, d = extra1(a, b)

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")

print(f"list1: {list1}")
print(f"list2: {list2}")

list3, list4 = extra2(list1, list2)

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list4: {list4}")
