# Ejercicio 30 - Registros de compras
# Aut@r: Jordi Casado
# Versión: 1.0

"""
ENUNCIADO:

1. Crea una tupla llamada **`compras_enero`** que contenga los precios de productos comprados durante el mes de enero.
2. Implementa la funcionalidad para calcular el total gastado en compras durante un mes.
3. Implementa la funcionalidad para encontrar el precio del producto más caro en una lista de precios.
4. Crea una tupla llamada **`compras_febrero`** con precios de productos comprados en febrero.
5. Utiliza el método **`count`** para contar cuántas veces se compró un producto específico en febrero.
6. Utiliza la función **`max`** para encontrar el precio más alto entre las dos tuplas.
7. Utiliza la función **`sum`** para calcular el gasto total en ambos meses.
8. Utiliza la función **`sorted`** para obtener una tupla ordenada de precios en ambos meses.
9. Imprime los resultados de las operaciones anteriores y verifica que las funcionalidades y métodos están trabajando correctamente.

"""

precios_enero = (10,35,58,39,25,10)

print(f" PRECIOS DE ENERO : {precios_enero}")

gasto_total = 0

for precio in precios_enero:
    
    gasto_total += precio
    print(f" El gasto total es: {gasto_total} ({precio}) € ")


print(f"\n Gasto Total del mes de enero: {gasto_total} €") # Gasto 

precio_mas_alto = max(precios_enero)

print(f"\n El precio más caro en la lista de precios es: {precio_mas_alto} € \n")

precios_febrero = 10,35,70,25,10,58

print(f" PRECIOS DE FEBRERO : {precios_febrero}\n")

print(f" Número de veces que se compró el artículo de precio 10: {precios_febrero.count(10)}\n")

pvp_max_tuplas = max(precios_enero + precios_febrero)

print(f" El precio máximo de los dos meses es de: {pvp_max_tuplas} € \n")

suma_gastos_totales = sum( precios_enero + precios_febrero)

print(f" La suma de gastos totales de ambos meses es de: {suma_gastos_totales} € \n")

tupla_ordenada_precios = sorted( precios_enero + precios_febrero)

print(f" El resultado de ordenar los precios de ambos meses es: {tupla_ordenada_precios} \n")








