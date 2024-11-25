#!/data/data/com.termux/files/usr/bin/python3

"""
* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
*   los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
*   (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
"""

__author__ = "zeidel garcia 'HaR3s'"
__maintainer__ = "Zeidel Garcia 'HaR3s'"
__email__ = "zeidel07.gatcia@gmail.com"
__vercion__ = "1.0"
__status__ = "Production"

# Lista

lista = [5, 4, 3, 2, 1]
# Tupla
tupla = (1, 2, 3, 4, 5)  # Las Tuplas son inmutales
# Diccionario
dicc = {"Uno": 1, "Dos": 2, "Tres": 3}
# Sets
sets = {1, 2, 3, 4, 5}  # Los Sets No se pueden ordenar

# Operaciones


# Mostrar por consola
print("Creacion")
print(f"\nLista: {lista}")
print(f"Diccionario: {dicc}")
print(f"Tupla: {tupla}")
print(f"Sets: {sets}")


# insercion
lista.append(10)
dicc["Cuatro"] = 4
sets.add(10)


# Mostrar por consola
print("\nIncercion")
print(f"\nLista: {lista}")
print(f"Diccionario: {dicc}")
print(f"Tupla: {tupla}")
print(f"Sets: {sets}")

# Eliminación
lista.remove(1)
sets.remove(1)
del dicc["Uno"]


# Mostrar por consola
print("\nEliminar")
print(f"\nLista: {lista}")
print(f"Diccionario: {dicc}")
print(f"Tupla: {tupla}")
print(f"Sets: {sets}")

# Acceso
print("\nAccediendo a un valor")
print(f"\nLista: {lista[3]}")
print(f"Sets: {sets}")
print(f"Diccionario: {dicc['Dos']}")
print(f"Tupla: {tupla[3]}")

# Ordenemiento
lista.sort()
tupla = tuple(sorted(tupla))
dicc = dict(sorted(dicc.items()))


# Mostrar por consola
print("\nOrdenar")
print(f"\nLista: {lista}")
print(f"Diccionario: {dicc}")
print(f"Tupla: {tupla}")
print(f"Sets: {sets}")

# Actualización
lista[0] = 1
dicc["Dos"] = 1

# Las Tuplas y Los Sets no se pueden Actualizar

# Mostrar por consola
print("\nActualizar")
print(f"\nLista: {lista}")
print(f"Diccionario: {dicc}")
print(f"Tupla: {tupla}")
print(f"Sets: {sets}")


# EXTRA
def agenda():
    agendaContact = {}  # Declaracion del diccionario que almacenara los datos

    def incertarContacto(contacto: str, numero: int):
        agendaContact[str.title(contacto)] = numero  # Añadir nuevo dato

    def buscarContacto(buscar):
        if (
            type(buscar) is str and buscar in agendaContact
        ):  # verificaca si el dato recivido es un string
            return agendaContact[
                str.title(buscar)
            ]  # Retorns el valor del dato recivido
        elif type(buscar) is int:  # verifica si el dato recivido es entero
            for n in agendaContact:  # recorre el diccionario
                if (
                    agendaContact[n] == buscar
                ):  # Verifica si el dato recivido coincide con la clave
                    return n  # Retorna la clave
        print("Datos no validos")

    def actualizarContacto(contacto, actualizar):
        agendaContact[str.title(contacto)] = (
            actualizar  # Actualiza el valor de la clave recivida
        )

    def eliminarContacto(contacto):
        print(
            f"Eliminando {str.title(contacto)} : {buscarContacto(str.title(contacto))}\nDone!!!"
        )
        del agendaContact[str.title(contacto)]  # Elimina un dato

    def showContact():
        cont = 0
        for n in agendaContact:
            cont += 1
            print(
                '{}\n{:>4}\n{:>14} "{}"\n{:>4},\n{:>4}\n{:>16} "{}"\n{:>4},\n{},'.format(
                    "{",
                    "{",
                    '"Nombre:"',
                    n,
                    "}",
                    "{",
                    '"Telefono:"',
                    agendaContact[n],
                    "}",
                    "}",
                )
            )
        print(f"\nHay {cont} congactos en la agenda\n")

    def menu():
        while True:
            print("{:>30}".format(" Agenda Telefonica"))
            print("""
            Opciones:

            1.) Incertar Contacto 
            2.) Buscar Contacto
            3.) Actualizar Contacto
            4.) Eliminar Contacto
            5.) Mostrar Contactos
            6.) Salir
            """)
            try:
                opcion = int(input("--> "))

                match opcion:
                    case 1:  # Opcion para incertar contacto
                        nombre = input("Introduzca el nombre del contacto\n--> ")
                        while True:
                            try:
                                numero = int(input("Introduzca el numero\n---> "))
                                if (
                                    0 < len(str(numero)) == 8
                                ):  # Comprobamos que el numero no es negativo y tiene 8 digitos
                                    incertarContacto(nombre, numero)
                                    break
                                else:
                                    print(
                                        "El numero no coincide con el formato de 8 digitos"
                                    )
                            except (
                                ValueError
                            ):  # Comprobamos que el numero recivido siempre sea entera
                                print("Error! Tipo de dato incorrecto")

                    case 2:  # Opcion de buscar contacto
                        print("Nombre o Telefono")
                        print("""
                    1.) Nombre
                    2.) Numero
                    """)
                        try:
                            num = int(input("---> "))
                            match num:
                                case 1:
                                    nombre = input("Nombre\n--> ")
                                    print(
                                        f"{str.title(nombre)} : {buscarContacto(nombre)}"
                                    )
                                case 2:
                                    buscarNumero = int(input("Numero\n--> "))
                                    if 0 < len(str(buscarNumero)) == 8:
                                        print(
                                            f"{buscarContacto(buscarNumero)} : {buscarNumero}"
                                        )
                                    else:
                                        print(
                                            "Error! el Formato no coincide debe de tener 8 digitos"
                                        )
                        except ValueError:
                            print("Opcion no valida\nRegresando al Menu Principal")
                    case 3:  # opcion de actualizar contacto
                        contacto = input("Contacto a actualizar: 'Nombre'\n--> ")
                        try:
                            if (
                                str.title(contacto) in agendaContact
                            ):  # verificamos si existe
                                actualizar = int(input("Nuevo numero\n--> "))
                                if 0 < len(str(actualizar)) == 8:
                                    actualizarContacto(contacto, actualizar)
                                else:
                                    print(
                                        "Error! el Formato no coincide debe de tener 8 digitos"
                                    )
                            else:
                                print("El contacto a actualizar no existe")
                        except TypeError:
                            print(
                                "Error! Introduzca un numero entero\nRegresando al Menu Principal"
                            )
                    case 4:  # Opcion de Eliminar
                        contactoElim = input("Contacto a elimiar: 'Nombre'\n--> ")
                        if (
                            str.title(contactoElim) in agendaContact
                        ):  # Verificamos que este en el Diccionario
                            eliminarContacto(contactoElim)
                        else:
                            print("Error! el contacto no existe")

                    case 5:
                        showContact()

                    case 6:  # Opcion de Salir
                        print("\nTenga un buen día")
                        break
            except ValueError:  # Comprobamos que la opcion recivida siempre sea entera
                print("Error! Solo numeros enteros")

    menu()


agenda()
