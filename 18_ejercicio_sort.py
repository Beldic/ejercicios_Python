# Ejercicio 18 - Programa que ordena edades (listas)
# Autor: Jordi Casado
# Versión 1.0
"""

Crea un programa que le solicite al usuario que piense en 4 familiares cercanos, y que introduzca las edades
de sus 4 familiares en 4 entradas por teclado diferentes que se almacenarán en una lista. 
Posteriormente devolveremos la información de salida con el formato correpondiente:

1. Inicializar las siguientes variables y asignar un valor de entrada por teclado: edad1, edad2, edad3 y edad4.

2. Ordenar las edades de forma ascendente y descendente utilizando el método sort(). Y también el método sorted().

3. Mostrar el resultado por salida utilizando el método print().

"""

# Yo le he hecho con append en vez de usar el método extend, ahorrando crear las cuatro variables.  ;)


lista_familiares = []

lista_familiares.append(input("Introduce la edad del primer familiar: "))
lista_familiares.append(input("Introduce la edad del segundo familiar: "))
lista_familiares.append(input("Introduce la edad del tercer familiar: "))
lista_familiares.append(input("Introduce la edad del  cuarto familiar: "))

lista_familiares.sort()

print(f" Lista de edad de familiares ordenada {lista_familiares} ")

lista_familiares.sort(reverse=True)

print(f" Lista de edad de familiares ordenada del revés {lista_familiares}")

nueva_lista = sorted(lista_familiares)


print(f" Nueva Lista de edad de familiares ordenada {nueva_lista}")

nueva_lista.sort(reverse=True)

print(f" Nueva Lista de edad de familiares ordenada del revés {nueva_lista} ")
