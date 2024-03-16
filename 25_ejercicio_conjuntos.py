# Ejercicio 25 - Discurramos sobre los conjuntos.
# Autor: Jordi Casado
# Versión: 1.0

"""
#1- **Crea dos conjuntos/sets nuevos y añádelos dentro de un tercer conjunto.**
	- Utilizando el método .union()
#2- **Accede a uno de los elementos de tu conjunto y modifícalo**
 - Los elementos en los conjuntos no son accesibles, como ocurre por ejemplo con las tuplas o las listas a cuyos elementos
   se puede acceder a través de un index. Dada la naturaleza de los conjuntos de no mantener el orden.

"""

A = {1, 2, 3}
B = {3, 4, 5}


D = A.union(B)  # Crea un conjunto D por unión de A y B

print(D) 

mi_lista = list(D) # Convierto mi conjunto D en una lista

print(mi_lista)

mi_lista[0] = 10  #  Modifico el primer elemento de la lista

D = set(mi_lista) # Vuelvo a convertir mi lista en el conjunto

print(D)