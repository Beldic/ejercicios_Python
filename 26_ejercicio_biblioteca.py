# Ejercicio 26 - Biblioteca de Videojuegos
# Autor : Jordi Casado
# Versión: 1.0

"""
Vamos a crear un programa en Python que simule la gestión de una biblioteca de videojuegos. Para ello, vamos a utilizar conjuntos para representar diferentes categorías de videojuegos y realizar operaciones sobre ellos.

1. Define los siguientes conjuntos para representar diferentes categorías de videojuegos:
    - **`aventura`**: Contiene videojuegos de aventura.
    - **`accion`**: Contiene videojuegos de acción.
    - **`estrategia`**: Contiene videojuegos de estrategia.
    - **`deportes`**: Contiene videojuegos de deportes.
2. Utiliza la función **`input()`** para permitir al usuario agregar videojuegos a cada categoría. Pídele al usuario que ingrese los nombres de los videojuegos separados por comas.
3. Convierte las cadenas ingresadas por el usuario en conjuntos utilizando el método **`split()`** y luego agregalos a los conjuntos correspondientes utilizando el método **`update()`**.
4. Muestra al usuario un resumen de las categorías de videojuegos y la cantidad de videojuegos en cada una utilizando la función **`print()`** y la función **`len()`** .
5. Utiliza operadores de conjuntos para realizar algunas operaciones como:
    - Mostrar los videojuegos que están presentes en la categoría de acción y aventura.
    - Mostrar los videojuegos que están presentes en la categoría de estrategia pero no en la de deportes.
    - Mostrar todos los videojuegos únicos presentes en todas las categorías.

Instrucciones adicionales:

- **Asegúrate de manejar correctamente la entrada del usuario (separadores, uso de mayúsculas y minúsculas) y realizar las conversiones necesarias de datos utilizando casting de datos.**
- Recuerda usar la función **`split()`** para dividir la entrada del usuario en elementos separados y el método **`update()`** para agregar elementos a los conjuntos.

"""


# BIBLIOTECA DE VIDEOJUEGOS


con_aventura = set() 
con_accion = set()
con_estrategia = set() 
con_deportes = set()


lis_aventura = (str(input("\nIntroduce los títulos de aventuras separados por coma(,): ")).upper())
lis_accion = (str(input("Introduce los títulos de acción separados por coma(,): ")).upper())
lis_estrategia = (str(input("Introduce los títulos de estrategia sepadados por coma(,): ")).upper())
lis_deportes = (str(input("Introduce los títulos de deportes separados por coma(,): ")).upper())

con_aventura.update(lis_aventura.split(","))
con_accion.update(lis_accion.split(","))
con_estrategia.update(lis_estrategia.split(","))
con_deportes.update(lis_deportes.split(","))

print("\n - RESUMEN DEL CATÁLOGO DE VIDEOJUEGOS -")

print(f"\n {len(con_aventura)} Títulos en AVENTURA: {con_aventura}")
print(f"\n {len(con_accion)} Títulos en ACCIÓN: {con_accion}")
print(f"\n {len(con_estrategia)} Títulos en ESTRATEGIA: {con_estrategia}")
print(f"\n {len(con_deportes)} Títulos de DEPORTES: {con_deportes}\n")

# OPERACIONES CON CONJUNTOS

print(f"\n Titulos presentes en Aventura y Acción: {con_aventura.union(con_accion)}")
print(f"\n Titulos presentes en Estrategia pero no en la de deportes: {con_estrategia.difference(con_deportes)}")

con_todos = set()

print(f"\n Todos los juegos en tu BIBLIOTECA DE JUEGOS: { con_todos.union(con_aventura,con_accion,con_estrategia,con_deportes)}")


        






