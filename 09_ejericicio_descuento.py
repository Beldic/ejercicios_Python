#Ejercicio9: Calculadora de descuento.
#Autor: Jordi Casado 
#Versión: 1.0

"""Desarrolla un programa en Python que permita calcular el precio final de un producto después de aplicar un descuento.

    1. Inicio del programa: 
        - Inicia el programa con un mensaje de bienvenida. 
    2. Entrada de datos:
        - Solicita al usuario ingresar el precio original del producto como un número decimal. 
    3. Entrada de descuento:
        - Pide al usuario que ingrese el porcentaje de descuento que desea aplicar al producto. 
    4. Cálculo del precio con descuento:
        -Calcula el precio final después de aplicar el descuento. 
        -Utiliza la fórmula: Precio_final = precio_original - (precio orginal * porcentaje de descuento / 100)
    5. Mostrar resultados:
        -Muestra el precio original, el porcentaje de descuento y el precio final después de aplicar el descuento
        -Utiliza f-strings para formatear los resultados y y mostrar el precio final con dos decimales. 
"""

print ("\n - Bienvenido al Chiringuito de la Programación - \n")

precio_original = float(input("\n Introduce el precio de la ración de espetos de sardinas:  \n"))
porcentaje_descuento = float(input("\n Introduce el porcentaje de descuento de la ración de espetos de sardinas:"))

precio_descuento = float(precio_original - (precio_original * porcentaje_descuento / 100))

print(f"\n El precio ogirinal es {precio_original} y el precio final con descuento {precio_descuento:.2f} \n")

print(f" ¡GRACIAS POR SU VISITA! ")

