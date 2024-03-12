#Ejercicio 23 - Tuplas y temperaturas

"""
Vamos a trabajar con una tupla que representa las termperaturas diarias de una ciudad durante
una semana. La tupla se llama temperaturas y contiene valores en grados Celsius. Realiza las 
siguientes tareas:

1. Crea una tupla llamada temperaturas con al menos 7 valores de temperaturas diarias. 

2. Imprime la longitud de la tupla. 

3. Utiliza el método count para determinar cuantas veces aparece la temperatura 25 en la tupla. 

4. Encuentra el índice de la primera aparición de la temperatura utilizando el método index. 

5. Crea una tupla llamada temperaturas_ordenadas que contenga las temperaturas ordenadas de
   manera ascendente de la tupla temperaturas. 

6. Concatena la tupla original con la nueva tupla  temperaturas_ordenadas. 

7. Repite la tupla original tres veces y almacénala en una nueva tupla llamada temperaturas_repetidas. 

8. Imprime todas las tuplas resultantes y observa los cambios. 

Nota: Asegúrate de utilizar los métodos y operadores vistos en clase. 





"""




temperaturas = 12,25,18,25,12,10,36

print(len(temperaturas))

print(temperaturas.count(25))

print(temperaturas.index(18))

temperatura_ordenada_lista = sorted(temperaturas) # <---?

print(temperatura_ordenada_lista)

temperatura_ordenada_lista.reverse()

print(temperatura_ordenada_lista)

temperatura_tupla = tuple(temperatura_ordenada_lista)

temperatura_concatenada = temperatura_tupla + temperaturas 

print(temperatura_concatenada)

temperaturas = temperaturas * 3

print(temperaturas)








