# Ejercicio 35 - Películas
# Autor: Jordi Casado
# Versión: 1.0

"""
ENUNCIADO: 

1. Define un diccionario vacio llamado **`peliculas`** Y solicita al usuario que agrege al menos cinco películas. Cada película debe tener un título como clave y su año de lanzamiento como valor. 
2. Utiliza un bucle **`for`** junto con el método **`keys()`** para iterar sobre el diccionario e imprimir solo los títulos de las películas.
3. Utiliza un bucle **`for`** junto con el método **`items()`** para iterar sobre el diccionario e imprimir tanto los títulos de las películas como sus años de lanzamiento.
4. Utiliza un bucle **`for`** junto con el método **`values()`** para iterar sobre el diccionario e imprimir solo los años de lanzamiento de las películas. Dentro del bucle, realiza las siguientes operaciones con los años de lanzamiento:
    - Comprueba si el año es mayor que 2000 utilizando un operador de comparación.
    - Comprueba si el año es divisible por 5 utilizando un operador de módulo (%).
    - Comprueba si el año es igual a 1995 utilizando un operador de comparación.
    - Asigna el año a una nueva variable y muéstralo junto con un mensaje personalizado.
5. Después de completar las iteraciones, muestra un mensaje de conclusión.
"""


peliculas = {     # He optado por crear el diccionario con algunas de mis pelis favoritas. 

    "The Gonnies" : 1980,
    "War Games" :  1983,
    "Contact" : 1997,
    "The Matrix" : 1999,
    "The Imitation Game" : 2014,
}

for titulo in peliculas.keys():   # 2:  Muestro los títulos de las películas

    print(titulo,"\n")

for titulo , year in peliculas.items(): # 3:  Itero sobre las claves y valores del diccionario para mostrarlos juntos

    print(titulo," : ", year)

valor = False 



for fecha in peliculas.values(): #4:  Itero sobre los valores del diccionario para obtener los años y sus características: 

    if (fecha > 2000):

        print(fecha, "Es una fecha posterior a 2000")

    else:
    
        print(fecha, "La fecha es anterior al año 2000")



    

    if(fecha % 5 > 0):

        print(fecha, "No es múltiplo  5")

    else:
    
        print(fecha,  "Es múltiplo 5")

    
    if (fecha != 1995):

        print(fecha, "no es igual al año 1995")

    else:

        print(fecha, "es igual al año 1995")


    var_fecha = fecha

    print(f" La fecha en cuestión es: {var_fecha} \n")
    
    

