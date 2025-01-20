#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
*
* DIFICULTAD EXTRA (opcional):
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

# Pilas LIFO

stack = [n**2 for n in range(0, 6)]

print(stack)

# POP

for i in range(len(stack)):
    item = stack.pop()
    print(f"Dell {item} at position {len(stack)}")

    print(f"\n{stack}\n")

# Cola FIFO

queue = [n**2 for n in range(5, 11)]

# dequeue

for i in range(len(queue)):
    item = queue.pop(0)
    print(f"Dell {item} at position {len(queue)}")

    print(f"\n{queue}\n")


def extra():
    def web():
        stack = []
        while True:
            inn = input(
                "Escriba la web que desee acceder o B/b'Atras' N/m'Adelante' X/x'Salir'\n-> "
            )

            if inn == "N" or inn == "n":
                pass
            elif inn == "B" or inn == "b":
                if len(stack) > 0:
                    try:
                        stack.pop()
                        print(f"As regresado a: {stack[len(stack) -1]}")
                    except IndexError:
                        print("Estas en la pagina de inicio")
                else:
                    print("Estas en la pagina de inicio")
            elif inn == "X" or inn == "x":
                break
            else:
                stack.append(inn)

    def imprimir():
        documentos = []
        while True:
            inn = input("I/i'imprimir X/x 'Salir -> ")

            if inn == "I" or inn == "i":
                for i in range(len(documentos)):
                    data = documentos.pop(0)
                    print(f"Imprimiendo: {len(documentos) + 1} documentos -> {data}")
            elif inn == "X" or inn == "x":
                break
            else:
                documentos.append(inn)

    web()
    imprimir()


extra()
