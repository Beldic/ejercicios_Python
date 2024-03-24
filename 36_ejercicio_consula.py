# Ejercicio 36 - Programa de consulta de colección de datos
# Autor: Jordi Casado 
# Versión: 1.0

"""
ENUNCIADO:

1. Crea cuatro diccionarios, uno para cada tipo de colección de datos: listas, tuplas, conjuntos y diccionarios.
2. Cada diccionario contendrá las siguientes claves con sus respectivos valores:
    - **Definición:** Una breve definición del tipo de colección de datos.
    - **Mutabilidad:** Una descripción de si la colección es mutable o inmutable.
    - **Acceso a elementos:** Una explicación de cómo se accede a los elementos en la colección.
    - **Tipos de datos:** Los tipos de datos que la colección puede contener.
    - **Orden:** Una descripción sobre si la colección mantiene el orden de los elementos.
    - **Duplicados:** Una explicación sobre si la colección permite elementos duplicados.
    - **Métodos:** Un diccionario anidado que incluya los métodos relevantes para cada tipo de colección, donde la clave será el nombre del método y el valor será una breve descripción de su función.
3. Cada diccionario debe estar almacenado en una variable con un nombre que represente el tipo de colección correspondiente (por ejemplo, **`diccionario`**, **`conjunto`**, **`listas`**, **`tuplas`**).
4. Implementa un programa que permita a los usuarios consultar la información sobre cada tipo de colección de datos.
    - El programa debe solicitar al usuario que introduzca el nombre de la colección de datos que desea consultar.
    - Luego, el programa mostrará todos los detalles y métodos asociados con la colección seleccionada.
"""

dic_lista  = {                  #Primer diccionario sobre lista
    "nombre": "lista",
    "Definición" : "Es una colección de datos",
    "Mutabilidad" :  "Se puede cambiar su contenido",
    "Tipos de datos" : "Cualquier tipo de dato",
    "Orden" : "Ordenable",
    "Duplicados: " : "Permite duplicar sus elementos",
    "Métodos" : {

        "Agregar": "append, insert, extend, update",
        "Borrar":"pop, remove, clear",
        "Consulta":"index, count",
        "ordenar": "sort, sorted"
    }


}

dic_tupla = {
    "nombre": "tupla",
    "Definición": "Es una colección de datos ordenada e inmutable",
    "Mutabilidad": "No se puede cambiar su contenido una vez creada",
    "Tipos de datos": "Cualquier tipo de dato",
    "Orden": "Ordenada",
    "Duplicados": "Permite duplicados",
    "Métodos": {
        "Consulta": "index, count"
    }
}

dic_conjunto = {
    "nombre": "conjunto",
    "Definición": "Es una colección no ordenada y sin elementos duplicados",
    "Mutabilidad": "Se puede cambiar su contenido, agregando o eliminando elementos",
    "Tipos de datos": "Solo tipos de datos inmutables",
    "Orden": "No ordenable",
    "Duplicados": "No permite duplicados",
    "Métodos": {
        "Agregar": "add, update",
        "Borrar": "pop, remove, discard, clear",
        "Consulta": "N/A",
        "Operaciones de conjuntos": "union, intersection, difference, symmetric_difference"
    }
}

dic_diccionario = {
    "nombre": "diccionario",
    "Definición": "Es una colección de datos no ordenada, que almacena pares de clave-valor",
    "Mutabilidad": "Se puede cambiar su contenido, agregando, actualizando o eliminando pares clave-valor",
    "Tipos de datos": "Cualquier tipo de dato para el valor, las claves deben ser inmutables",
    "Orden": "Ordenable a partir de Python 3.7, por orden de inserción",
    "Duplicados": "No permite duplicados en las claves, pero sí en los valores",
    "Métodos": {
        "Agregar": "update, setdefault",
        "Borrar": "pop, popitem, clear",
        "Consulta": "keys, values, items",
        "Otros": "get, copy"
    }
}


consulta = str(input("introduce el tipo de colección de dato a mostrar (lista, tupla, conjunto, diccionario): "))    # Introduzco la consulta del tipo de colección de datos a mostrar

lista = [dic_lista, dic_tupla, dic_conjunto, dic_diccionario]  # creo una lista que englobe las listas  anteriormente definidas


print(consulta)

for diccionario in lista:     # Recorro la lista recién creada y los elementos (listas) de los misma, con un bucle for anidado. 

    for clave in diccionario.values():

        if (clave == consulta): 

            print(diccionario)

            break


        else:

            print(f"¡{clave} no encontrado!")

            break



    break