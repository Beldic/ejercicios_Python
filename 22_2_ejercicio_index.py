"""Práctica:
tupla_practica = 1, 2, 3, 50, 60, 70, 1, 2, 3, 50, 60, 70
 1- ¿Cuál es el index de la primera ocurrencia de 60?
 2- ¿Cuál es el index de la segunda ocurrrencia de 60?
 3- ¿Cuál es el index de la segunda ocurrencia de 2?
 4- ¿Cuál es el index de la primera ocurrencia de 3, entre los index 1 y 7?
"""

tupla_practica = 1, 2, 3, 50, 60, 70, 1, 2, 3, 50, 60, 70

print(tupla_practica)

indice = tupla_practica.index(60) 

print("1- Index de la primera ocurrencia de 60:", indice)

indice_dos = tupla_practica.index(60, indice +1 )

print("2- Index de la segunda ocurrencia de 60:", indice_dos)

indice_2_primera = tupla_practica.index(2)
indice_2_segunda = tupla_practica.index(2, indice_2_primera +1)

print("3- Index de la segunda ocurrencia de 2:",indice_2_segunda)

indice_3_entre1y7 = tupla_practica.index(3,1,8)

print("4- Index de la primera ocurrencia de 3, entre los index 1 y 7:", indice_3_entre1y7)

