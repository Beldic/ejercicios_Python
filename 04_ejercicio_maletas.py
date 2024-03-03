
# Ejercicio 4: Planificación de maletas para vacaciones.
# Autor: Jordi Casado
# Versión: 1.0

""" Instrucciones:

Ayuda al usuario a planificar sus maletas para las vacaciones.
Pídele que introduzca la información de los objetos que deben
incluirse en diferentes maletas. Al final, muestra toda la información
de manera ordenada.
 1. Pide al usuario que introduzca la información para cada maleta:
		- accesorios
		- ropa
		- tecnología
		- zapatos & zapatillas.

2. Cuando el usuario terminado de introducir la información, le va a devolver
los resultados en 4 listas diferentes, con toda la información en minúsculas,
y el título de cada lista en mayúsculas:
		LISTA ACCESORIOS
		accesorio 1, 
		LISTA ROPA
		LISTA TECNOLOGÍA
		LISTA ZAPATOS & ZAPATILLAS"""






print("\nEstimado viajer@, bienvenid@ a las Aerolíneas Adecco, introduzca la información de las maletas a facturar:\n")

maleta_accesorios = str(input("Artículos de la maleta accesorios: \n "))
maleta_ropa = str(input("Artículos de la maleta con ropa:\n  "))
maleta_tecnologia = str(input("Artículos de la maleta tecnología \n "))
maleta_zapatos = str(input("Artículos de la maleta zapatos \n "))

print(f" - INFORMACIÓN DEL EQUIPAJE - \n MALETA ACCESORIOS: {maleta_accesorios.lower()} \n MALETA ROPA: {maleta_ropa.lower()} \n MALETA TECNOLOGÍA: {maleta_tecnologia.lower()} \n MALETA ZAPATOS: {maleta_zapatos.lower()} \n")



