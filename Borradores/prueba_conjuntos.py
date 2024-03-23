
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

"""

F = {2,5,8,3}

print(F)

for numero in F: 

    if numero == 2:

        F.discard(7) # o remove, 
        break


print(F)

longitud = len(F)

print(longitud)

H = F.copy()

print(H)

cadena = "El gato es blanco"

cadena = "1,2,3,4,5"

print(cadena.split(","))

R = {1,2,3}
lista = [5,6]
T = R.update(lista)
print(R)






