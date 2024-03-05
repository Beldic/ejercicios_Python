# Ejercicio12: Calculadora de propinas. 
# Autor: Jordi Casado
# versión: 1.0

"""
Desarrolla un programa en Python que permita calcular la propina a dejar en un restaurante. El ejercicio
se centrará en practicar operaciones aritméticas básicas, la entrada de datos desde el teclado, la 
conversión de datos mediante casting, y la presentación de resultados utilizando f-strings. 

1. Inicio del programa
    # Inicia el programa con un mensaje de bienvenida. 
2. Entrada de datos
    # Solicita al usuario que ingrese el monto total de la factura del restaurante como un número decimal. 
3. Entrada de porcentaje de propina:
    # Pide al usuario que ingrese el porcentaje de propina que dese dejar. 
4. Cálculo de la propina:
    #Calcula la propina a partir del monto total y el procentaje ingresado. Utiliza la fórmula:
        Propina = Monto Total * (Porcentaje de propina / 100)
5. Mostrar resultados
    # Muestra el monto total de la factura, el porcentaje de propina y el monto total a pagar incluyendo la propina. 
    # Utiliza f-strings para formatear los resultados y mostrar montos con dos decimales. 

"""


print("\n BIENVENIDO AL CHIRINGUITO PACO \n")

factura = float(input("Introduce el monto total de la factura: "))
porcentaje = float(input("\nIntroduce el porcentaje de propina que deseas dejar: "))

propina = factura * ( porcentaje / 100 )

print(f"\n La factura es: {factura:.2f} \n El porcentaje de propina es:{porcentaje:.2f} \n La propina es: {propina:.2f} \n y el monto final es: {(factura + propina):.2f}\n")