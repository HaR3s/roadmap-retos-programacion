#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
*   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
*   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
*   que representen todos los tipos de estructuras de control que existan
*   en tu lenguaje:
*   Condicionales, iterativas, excepciones...
* - Debes hacer print por consola del resultado de todos los ejemplos.
*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

# Operadores Aritméticos
a = 10
b = 3
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División Entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

# Operadores de Comparación
print(f"Igualdad: {a} == {b} = {a == b}")
print(f"Desigualdad: {a} != {b} = {a != b}")
print(f"Mayor que: {a} > {b} = {a > b}")
print(f"Menor que: {a} < {b} = {a < b}")
print(f"Mayor o igual que: {a} >= {b} = {a >= b}")
print(f"Menor o igual que: {a} <= {b} = {a <= b}")

# Operadores Lógicos
x = True
y = False
print(f"AND lógico: {x} and {y} = {x and y}")
print(f"OR lógico: {x} or {y} = {x or y}")
print(f"NOT lógico: not {x} = {not x}")

# Operadores de Asignación
c = 5
# c = c + 2
print(f"Asignación con suma: {c} += 2 = {c + 2}")
c += 2
print(f"Resta en Asignación: {c} -= 2 = {c - 1}")
c -= 1
print(f"Asignación con multiplicación: {c} *= 2 = {c * 3}")
c *= 3  # c = c * 3
print(f"Dicicion en Asignación: {c} /= 2 = {c / 2}")
c /= 2
print(f"Potencia en Asignación: {c} **= 2 = {c ** 2}")
c **= 2
print(f"División Entera en Asignación: {c} //= 2 = {c // 3}")
c //= 3
print(f"Residuo en Asignación: {c} %= 2 = {c % 2}")
c %= 2


# Operadores de Identidad
print(f"Es el mismo objeto: {a} is {b} = {a is b}")
print(f"No es el mismo objeto: {a} is not {b} = {a is not b}")

# Operadores de Pertenencia
lista = [1, 2, 3, 4, 5]
print("Pertenencia (2 en lista): ", 2 in lista)
print("Pertenencia (6 no en lista): ", 6 not in lista)

# Operadores a Nivel de Bits
print(f"AND a nivel de bits: {a} & {b} = {a & b}")
print(f"OR a nivel de bits: {a} | {b} = {a | b}")
print(f"Desplazamiento a la izquierda: {a} << 1 = {a << 1}")
print(f"Desplazamiento a la derecha: {a} >> 1 = {a >> 1}")

# Estructura Condicional
n = 10
if n > 0:
    print("n es positivo")
elif n == 0:
    print("n es cero")
else:
    print("n es negativo")

# Estructura Iterativa (Bucle For)
for i in range(3):
    print(f"Bucle For, iteración {i}")

# Estructura Iterativa (Bucle While)
contador = 3
while contador > 0:
    print(f"Contador: {contador}")
    contador -= 1

# Manejo de Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! División por cero.")
finally:
    print("Bloque finally ejecutado.")

# DIFICULTAD EXTRA
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
