#Ejercicio 24 - Operaciones con conjuntos
#Autor: Jordi Casado
#Versión 1.0

"""
Crea dos conjuntos A y B, imprimelos por pantalla y realiza las operaciones de unión, intersección,
diferencia, y diferencia simétrica. Además crea un tercer conjunto C y establece la relación de 
subconjunto y superconjunto con el conjunto A. 

"""


A = {1, 2, 3}
B = {3, 4, 5}


print("A",A,"B",B)

union = A.union(B)
print("Unión:", union)

interseccion = A.intersection(B)
print("Intersección:", interseccion)

diferencia = A.difference(B) # Solo los elementos que tiene A y no B
print("Diferencia (A - B):", diferencia)

# La diferencia simétrica contiene todos los elementos
# que están en alguno de los conjuntos, pero no en su intersección.

diferencia_simetrica = A.symmetric_difference(B)
print("Diferencia simétrica:", diferencia_simetrica)

C = {1, 2}

print("C",C)

es_subconjunto = C.issubset(A)
print("C es subconjunto de A:", es_subconjunto)


es_superconjunto = A.issuperset(C)
print("A es superconjunto de C:", es_superconjunto)