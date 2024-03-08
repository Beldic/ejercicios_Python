



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
