#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
* en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
* - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
*   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

from functools import partialmethod


cadena = "Hola"

# Acceso a caracteres específicos
print(cadena[0])

# Subcadenas

# Longitud
print(len(cadena))

# Concatenación
print(cadena + " Mundo")

# Repeticion
print(cadena * 3)

# Recorrido
for i in cadena:
    print(i, end=" ")
print()

# Convercion a mayúsculas
print(str.upper(cadena))

# Convercion a minúsculas
print(str.lower(cadena))

# Titulo en mayúsculas
print("hola mundo".title())

# Primer caracter en mayúsculas
print("hola mundo".capitalize())

# Reemplazo
print(cadena.replace("o", "a"))

# Union


# Divicion
print(cadena.split("l"))

# Interpolacion


# Verificacion


# Slicing
print(cadena[1:4])
print(cadena[2:])
print(cadena[0:2])
print(cadena[:-1])


# Eliminación de espacios al principio y al final
print(" Hola Mundo ".strip())

# Búsqueda al principio y al final
print(cadena.startswith("Ho"))
print(cadena.startswith("la"))

# Busqueda en una cadena
cadena2 = "Hola Mundo desde el lenguaje python"

print(cadena2.find("lenguaje"))
print(cadena2.find("python"))
print(cadena2.lower().find("py"))
print(cadena2.upper().find("H"))

# Búsqueda de ocurrencias
print(cadena2.lower().count("n"))

# Formateo
print("Saludo: {}, lenguje: {}!".format(cadena, cadena2[29:]))

# Interpolación
print(f"Saludo: {cadena}, lenguje: {cadena2[29:]}!")

# Tranformación en lista de caracteres
print(list(cadena))

# Transformación de lista en cadena
lista = [cadena, ", ", cadena2, "!"]
print("".join(lista))

# Transformaciones numéricas
charInt = "123456"
charInt = int(charInt)
print(charInt)

charFloat = "123456.123"
charFloat = float(charFloat)
print(charFloat)

# Comprobaciones varias
charNum = "123456"
print(charNum.isalnum())
print(charNum.isalpha())
print(charNum.isnumeric())


def Extra():
    def palindromo(cadena) -> bool:
        cad = cadena
        return True if str.lower(cad) == str.lower(cadena[::-1]) else False

    def anagrama(cadena: str) -> bool:
        cad = cadena
        return True if sorted(cad) == sorted(cadena) else False

    def isograma(cadena: str) -> bool:
        pass

    print(f"Ana es palindromo {palindromo("Ana")}")
    print(f"Ana es anagrama {anagrama("Ana")}")
    # print(f" es isograma {isograma("pythonpythonpython")}")


Extra()
