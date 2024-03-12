#Ejercicio 20 - reto de programación en grupo
#Autores: Jose Luis, Jordi, Roberto y Fran. 
#Versión 1.0 



"""
Bienvenidos al primer reto de programación del curso. Para este reto, al ser un ejercicio en grupo, el objetivo es que utilicéis no solo los conocimientos que habéis adquirido, si no también vuestra imaginación. 

El reto consiste en crear un programa, de temática libre, que incluya en la lógica del programa toda la sintaxis que hemos visto hasta ahora. A saber:

- Métodos de entrada y salida de información: print() e input()
- Métodos para formateo de cadenas de caracteres: lower() y upper()
- Operadores de Python
- Colecciones de datos: listas
- Bucle for iterando sobre una lista
"""
# Bienvenida a nuestra fruteria

print("\nBienvenido a la Frutería La Loly\n")

# Tema del ejercicio 
num_frutas = [1, 2, 3, 4, 5]
lista_frutas = []

# Introduce cinco frutas.
for indice in num_frutas:
    lista_frutas.append(input("Elige una fruta: "))
    print ("Tienes las siguientes frutas:", lista_frutas)
        
print (f"\nCompraste siguientes frutas: {lista_frutas}") 

for fruta in lista_frutas:
    print(f"Original: {fruta}")
    print(f"Mayúsculas: {fruta.upper()}")
    print(f"Minúsculas: {fruta.lower()}")
    longitud = len(fruta)
    print(f"Longitud: {longitud}")
    print(f"El doble de su longitud: {longitud * 2}")
    print("-" * 20)


#Conversión mayúsculas y minúsculas

print("Tu lista de frutas es:", lista_frutas)

#Operadores de Python










