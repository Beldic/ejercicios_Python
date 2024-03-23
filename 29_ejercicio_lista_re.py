# Ejercicio 29 - Gestión de listas de reproducción
# Autor: Jordi Casado
# Versión: 1.0

"""

ENUNCIADO: 

Vamos a crear un programa que gestione listas de reproducción de música utilizando conjuntos y las funciones/métodos que hemos aprendido.

1. Define dos listas de reproducción iniciales, **`playlist_a`** y **`playlist_b`**, cada una con al menos cinco canciones representadas por nombres de canciones (strings).
2. Crea conjuntos a partir de estas listas de reproducción.
3. Implementa la funcionalidad para agregar una nueva canción a una lista de reproducción.
4. Implementa la funcionalidad para eliminar una canción de una lista de reproducción.
5. Utiliza el método de conjunto **`union`** para crear una nueva lista de reproducción que contenga todas las canciones de **`playlist_a`** y **`playlist_b`**.
6. Utiliza el método de conjunto **`intersection`** para crear una nueva lista de reproducción que contenga solo las canciones que están en ambas **`playlist_a`** y **`playlist_b`**.
7. Utiliza el método de conjunto **`difference`** para crear una nueva lista de reproducción que contenga las canciones que están en **`playlist_a`** pero no en **`playlist_b`**.
8. Imprime las listas de reproducción resultantes y verifica que las funcionalidades y métodos están trabajando correctamente.


"""


playlist_a = ['Imagine', 'Puede Ser', 'Dulce Locura','Hotel California','Blowin in the wind','Granada' ]
playlist_b = [ 'Respect', 'Sweet Home Alabama', 'El Blues del Autobús','Granada','Vuelve']

# Crea los conjuntos a partir de la lista

conjunto_a = set(playlist_a)
conjunto_b = set(playlist_b)

# Agrega una nuevo elemento al conjunto_a

print(f"\n -LISTAS DE REPRODUCCIÓN- \n A: {conjunto_a} \n B: {conjunto_b} ")

nueva_cancion = str(input("\nIntroduce el título de una nueva canción: "))

print(f"Canción añadida: {nueva_cancion}")

conjunto_a.add(nueva_cancion)

cancion_eliminada = str(input("\nIntroduce el título de una canción de la lista a eliminar: "))

conjunto_a.remove(cancion_eliminada)

print(f"Canción eliminada: {cancion_eliminada}\n")

conjunto_ab_union = conjunto_a.union(conjunto_b) # Unión de conjuntos

print("\nUnión de A y B: ", conjunto_ab_union)

conjunto_ab_inter = conjunto_a.intersection(conjunto_b) # Intersección de conjuntos

print("\nIntersección de A y B: ", conjunto_ab_inter)

conjunto_ab_difer = conjunto_a.difference(conjunto_b) # Conjunto A - Conjunto B

print("\nDiferencia de A y B: ",conjunto_ab_difer)

print (f"\n Lista de reproducción A (actualizada): { conjunto_a}, \n Lista de reproducción B (actualizada): {conjunto_b} \n")












