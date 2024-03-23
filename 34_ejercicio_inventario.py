# Ejercicio 34 - Gestión de inventario
# Autor: Jordi Casado
# Versión: 1.0
"""
ENUNCIADO:

1. **Inicialización del inventario:**
    - Crea una lista llamada **`inventario`** que contendrá tuplas representando los productos en stock. Cada tupla contendrá el nombre del producto, su precio y la cantidad disponible en la tienda.
    - Agrega al menos 5 productos al inventario.
2. **Operaciones del inventario:**
    - Agrega un nuevo producto al inventario especificando su nombre, precio y cantidad.
    - Actualiza la cantidad disponible de un producto existente en el inventario.
    - Elimina un producto del inventario.
    - Busca un producto en el inventario y muestra su información si está disponible.
3. **Operaciones adicionales:**
    - Ordena el inventario alfabéticamente por nombre de producto.
    - Cuenta cuántos productos tienes en el inventario.
    - Encuentra la posición de un producto específico en el inventario.
4. **Mostrar resultados:**
    - Después de cada operación, muestra el inventario actualizado con todos los productos y su información.
    - Al final, muestra el inventario completo una última vez antes de finalizar el programa.
    - Puedes dar formato de salida a la muestra de inventario para que simule una tabla utilizando caracteres especiales.















"""









inventario = [
    
    ("ratón", 40, 10),
    ("pantalla", 900,15),
    ("teclado", 70,2)
    
]

print(inventario)

tupla = ("computadora", 1200,5)  # Creo una nueva tupla

nuevo_producto = inventario.append(tupla) # La añado a la lista de inventario 

print(inventario)

tupla_modificada = ("ratón", 80, 30) # Creo una tupla  <------------------------------------------

inventario[0] = tupla_modificada # me posiciono en la lista, en la índice 0 y modifico la tupla. 

print(inventario)

tupla_a_borrar = inventario[0]  #  Elimino el primer elemento de la lista (que es una tupla).

inventario.remove(tupla_a_borrar)

print(inventario)

#Busca un producto del inventario y muestra su información si está disponible:

producto_buscado = "pantalla" # Especifico que quiero buscar un raton

for producto in inventario:

    for nombre_producto in producto:

        if producto_buscado == nombre_producto: 

            print(producto)

            break

        
      
      # Busco si  hay alguna tupla que contenga la palabra "pantalla" 



# ordenado el inventario alfabeticamente

inventario_ordenado = sorted(inventario)

print(inventario_ordenado)

# numero de productos en el inventario 

cantidad_inventario = len(inventario)

print(cantidad_inventario)

#Encuentra la posición de un producto específico en el inventario

producto_especifico = "pantalla"

for posicion in inventario:

    for producto_actual in posicion:

        if producto_especifico == producto_actual:

            print(posicion.index(producto_actual))

            break
    

# Mostrar todos los datos del inventario. 
        
print(inventario)




    





