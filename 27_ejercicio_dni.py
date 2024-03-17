# Ejercicio 27 - Registrar los datos de un usuario para renovar su DNI
# Autor: Jordi Casado
# Versión: 1.0

"""
Enunciado:

Crea 3 diccionarios, utilizando las 3 versiones para crear diccionarios que hemos visto en clase
(sintaxis básica, y las dos versiones del método de constructor dict()). Rellena los datos de cada
diccionario con información que luego pediremos al usuario que actualice.. 

    1. El primer diccionario incluirá los datos básicos del usuario: Nombre, apellidos, fecha 
    de nacimiento , ciudad de nacimiento, nombre del padre y nombre de la madre. 

    2. El segundo diccionario incluirá: Nº de DNI, fecha de expedición y fecha de caducidad

    3. El tercer diccionario: Nacionalidad y domicilio. 

A continuación realiza las siguientes operaciones:

    1. Mostraremos los datos antiguos del diccionario. 

    2. El programa le pedirá al usuario que actualice los datos uno a uno utilianzado la función input()

    3. Por último le mostraremos al usuario los datos actualizados de los 3 diccionarios. 





"""


primer_diccionario = {

    "Nombre": "Pepe",
    "Apellidos": "Gordillo Moreno",
    "Fecha_nacimiento": "15/04/1986",
    "Ciudad_nacimiento": "Madrid",
    "Padre": "Juan Gordillo",
    "Madre": "María Moreno"

}

segundo_diccionario = dict(

    DNI = 37493942,
    Fecha_expedicion="15/05/1990",
    Caducidad="15/05/2025"


)

tercer_diccionario = dict([

    ("País","España"), 
    ("domicilio",  "calle falsa 123, Madrid")



])

print("\nDatos Antiguos: ")

for diccionario in [primer_diccionario,segundo_diccionario,tercer_diccionario]:

    for clave, valor in diccionario.items(): 

        print(f" {clave}:{valor} ") 



print("\n Introduce los datos: ")

for clave in primer_diccionario.keys():

    primer_diccionario[clave] = input(f" Actualiza {clave} (Anteriormente {primer_diccionario[clave]}): ")


for clave in segundo_diccionario.keys():

    segundo_diccionario[clave] = input(f" Actualiza {clave}: (Anteriormente {segundo_diccionario[clave]})")

for clave in tercer_diccionario.keys():

    tercer_diccionario[clave] = input(f" Actualiza {clave}: (Anteriormente {tercer_diccionario[clave]})")


print(f"\n Los datos actualizados son: ")


for diccionario in [primer_diccionario, segundo_diccionario, tercer_diccionario]:

    for clave, valor in diccionario.items():

        print(f" {clave}: {valor} ")












