# Ejercicio 44 - Los invitados de mi fiesta
# Autor: Jordi Casado
# Versión: 1.0

"""
ENUNCIADO:

Vamos a crear un programa que registre los nombres de los invitados a una fiesta. El programa solicitará al usuario que introduzca el nombre de cada invitado y lo agregará a una lista. Cuando el usuario escriba "fin", el programa mostrará la lista de invitados y terminará.

Instrucciones:

1. Inicia el programa con un mensaje de bienvenida.
2. Crea una lista vacía llamada **`invitados`**.
3. Utiliza un bucle **`while`** para solicitar al usuario que introduzca el nombre de un invitado.
4. Dentro del bucle, agrega cada nombre introducido por el usuario a la lista **`invitados`**.
5. Si el usuario escribe "fin", sal del bucle.
6. Después de salir del bucle, muestra un mensaje de despedida y la lista de invitados.

"""

invitados = []      # Creo una lista de invitados vacia


print("\n - BIENVENID@ AL PYTHON FESTIVAL 2025 - \n")   # Bienvenida

while True:  # Bucle infinito

    invitados.append(str(input("Introduce el nombre de un invitado o la palabra FIN:  ").upper()))   # invitado a la lista!

    if invitados[-1] == "FIN":  # Si el último invitado es igual a FIN 

        invitados.pop()  # Elimina "FIN" como último elemento de la lista 

        print("\n - LISTA DE INVITADOS - \n", invitados, "\n FIN DE LA APLICACIÓN")  # Imprime la lista de invitados y final

        break  # sale del bucle