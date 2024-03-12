"""Ejercicio de andar por casa -
Crea una colección de datos inmutable, que me permita añadir los siguientes datos de usuario:
- Nombre y apellidos
- Edad
- Ciudad de nacimiento
- Ciudad de residencia."""
#----------------------------------------------------------------------------------------------------
# Ejercicio de reflexión 
# Autor: Jordi Casado
# Versión: 1.0

nombre = []
apellido = []
edad = []
ciudad_natal = []
ciudad_residencia = []

nombre.append( input("Introduce tu nombre: "))
apellido.append(input("Introduce tu apellido: "))
edad.append(int("introduce tu edad: "))
ciudad_natal.append(input("Introduce tu ciudad natal: "))
ciudad_residencia.append(input("Introduce tu ciudad de residencia: \n"))



mi_tupla =(nombre, apellido, edad, ciudad_natal, ciudad_residencia) 

print(mi_tupla)

mi_tupla[0][0] = "Bartolo"

print(mi_tupla)


#------------------------------------------------------------------------------------------------------




