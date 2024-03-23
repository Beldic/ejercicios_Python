# Ejercicio 33 - Mezclum colección de datos
# Autor: Jordi Casado
# Versión: 1.0

"""
ENUNCIADO:

Crea un programa que gestione una lista de tareas pendientes, un conjunto de elementos de una lista de compras y un diccionario de contactos. 

1. **Creación de las Colecciones de Datos:**
    - Inicia el programa creando las siguientes colecciones de datos:
        - Una lista llamada **`tareas_pendientes`** que contenga al menos 5 tareas pendientes.
        - Un conjunto llamado **`lista_compras`** que incluya los elementos de una lista de compras con al menos 5 ítems.
        - Un diccionario llamado **`agenda_contactos`** que contenga los nombres y números de teléfono de al menos 5 contactos.
2. **Operaciones con la Lista de Tareas Pendientes:**
    - Utiliza el método **`append()`** para agregar una nueva tarea a la lista de tareas pendientes.
    - Utiliza el método **`remove()`** para eliminar una tarea específica de la lista de tareas pendientes.
    - Utiliza el método **`sort()`** para ordenar las tareas pendientes alfabéticamente.
    - Utiliza el método **`clear()`** para vaciar la lista de tareas pendientes.
3. **Operaciones con el Conjunto de la Lista de Compras:**
    - Utiliza el método **`add()`** para agregar un nuevo ítem a la lista de compras.
    - Utiliza el método **`discard()`** para eliminar un ítem específico de la lista de compras.
    - Utiliza el método **`clear()`** para vaciar el conjunto de la lista de compras.
4. **Operaciones con el Diccionario de Contactos:**
    - Utiliza el método **`update()`** para agregar nuevos contactos al diccionario de contactos.
    - Utiliza el método **`sorted()`** para ordenar los contactos por nombre y mostrarlos en orden alfabético.
    - Utiliza el método **`pop()`** para eliminar un contacto específico del diccionario de contactos.
    - Utiliza el método **`clear()`** para vaciar el diccionario de contactos.
5. **Mostrar Resultados:**
    - Después de cada operación, muestra el estado actual de cada colección de datos.
6. **Finalizar el Programa:**
    - Proporciona una opción para que el usuario pueda salir del programa cuando lo desee.


"""

tareas_pendientes = ["sacar a Tobi","comprar acciones","realizar OPA hostil","lavar el Ferrari"]

lista_compras = { "aceite", "arroz", "mermelada", "pasta de dientes", "Cola Cao"}

agenda_contactos = { 

    "Vane" : "312567890",
    "Luca" : "456789012",
    "Tobi" : "123456789",
    "Susi" : "987654321",
    "Javi" : "555555555"

}

# Operaciones con la lista tareas pendientes.

print(tareas_pendientes)

tareas_pendientes.append("Despedir al mayordomo")

print(tareas_pendientes)

tareas_pendientes.remove("sacar a Tobi")

print(tareas_pendientes)

tareas_pendientes.sort()

print(tareas_pendientes)

tareas_pendientes.clear()

print(tareas_pendientes)

# Operaciones con el Conjunto de la Lista de Compras:

print(lista_compras)

lista_compras.add("Ferrero Roché")

print(lista_compras)

lista_compras.remove("arroz") # discard

print(lista_compras)

lista_compras.clear()

print(lista_compras)

# Operaciones con el Diccionario de contactos:

print(agenda_contactos) 

agenda_contactos.update("Susi") 

print(agenda_contactos)

agenda_contactos.pop("Javi")

print(agenda_contactos)

agenda_contactos.sorted()

print(agenda_contactos)

agenda_contactos.clear()

print(agenda_contactos)

