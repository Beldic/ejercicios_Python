# Ejercicio 19 - Programa de gestión de tareas (listas)
# Autor: Jordi Casado
# Versión: 1.0

"""
Crea un programa en Python que simule la gestión de tareas pendientes. 
1. Utiliza una lista para almacenar las tareas y realiza las siguientes operaciones:

    a. Agregar tres tareas de forma simultánea al final de la lista. 
    b. Mostrar todas las tareas actuales. 
    c. Verificar si una tarea específica, tarea_buscar, está presente en vuestra lista.
    d. Eliminar la segunda tarea de la lista.
    e. Mostrar el número de tareas después de eliminar la del punto d. 

"""

lista_tareas = []   # crear lista 

tarea_1 = 1     
tarea_2 = 2
tarea_3 = 3

lista_tareas.extend([tarea_1,tarea_2, tarea_3])   #a

print(f" Tareas: {lista_tareas}")       #b
 
tarea_buscar = input(" Introduce la tarea a buscar: ")


if tarea_buscar in lista_tareas:   #c

    print(f" La tarea {tarea_buscar} esta en  {lista_tareas}")

else:

    print(f" La tarea {tarea_buscar} no esta en {lista_tareas}")



lista_tareas.remove(lista_tareas[1]) #d

print(f" Tareas pendientes: {len(lista_tareas)}") #
