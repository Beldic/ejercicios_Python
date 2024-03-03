#Ejercicio10: Programa de información personal. 
#Autor: Jordi Casado
#Versión: 1.0

"""
Crea un programa en Python que solicite al usuario ingresar su información personal, incluyendo su nombre
,edad y cidudad de residencia. Luego, utiliza la función print() para mostrar un mensaje personalizado 
utilizando diferentes métodos de formateo de cadenas. 

1. Solicita al usuario que introduzca su nombre. 
2. Solicita al usuario que introduzca su edad. 
3. Solicita al usuario que introduzca su ciudad de residencia. 

Luego, muestra un mensaje de saludo personalizado que incluya la información ingresada. Utiliza tanto la
función .format() como las f-strings para formatear la salida de la siguiente manera:

* En el primer mensaje, utiliza .format() para incluir el nombre y la ciudad. 
* En el segundo mensaje, utiliza una f-string para incluir la edad. 

"""


print("\n ¡Bienvenido al Programa de Información Personal! \n")

nombre = str(input("\n Introduce tu nombre: "))
edad = str(input("\n Introduce tu edad: "))
ciudad = str(input("\n Introduce tu ciudad de residencia: "))

print("\n ¡Hola, {}! Bienvenido a {}. ".format(nombre,ciudad)+f"\n Esperamos que disfrutes de tu estudio, tienes {edad} años de sabiduaría.\n")


