# Ejercicio 15: Calculadora de impuestos para autónomos
# Autor: Jordi Casado
# Versión: 1.0

"""
Desarrolla un programa en Python que ayude a un autónomo a calcular los impuestos que 
deberá pagar en un trimestre. 
1. Inicio del programa. 
    # Inicia el programa con un mensaje de bienvenida para el autónomo. 
2. Entrada de datos. 
    # Solicita al autónomo los siguientes datos: 
    - Ingresos totales del trimestre como un número decimal.
    - Gastos deducibles del trimestre como un número decimal. 
    - Otros gastos no deducibles del trimestre como un número decimal. 
3. Cálculo de la base imponible. 
    # Calcula la base imponible restando los gastos deducibles y otros gastos no deducibles a los 
    ingresos totales del trimestre. 
4. Cálculo del impuesto a pagar.
    # Calcula el impuesto a pagar como el  10% de la base imponible.
5. Mostrar Resultados:
    # Muestra los siguientes resultados:
    - Ingresos totales. 
    - Gastos deducibles. 
    - Otros gastos no deducibles. 
    - Base Imponible.
    - Impuesto a pagar.
6. Consideraciones Adicionales:

    #Utiliza f-strings para formatear los resultados y mostrar montos con dos decimales. 
    #No es necesario utilizar la estructura de control if en este ejercicio. 

"""

nombre = str(input("\n Introduce tu nombre o razón social: "))

print(f"############################")
print(f"#   -CONTABLE AL DIA-      #")
print(f"############################")

print(f"\n #Recibe la bienvenida, {nombre.upper()}. \n #A continuación pasaremos a la recopilación de datos... ")

ingresos_totales = float(input((f"\n# A)INGRESOS TOTALES\n"))) 
gastos_deducibles = float(input(f"# B)GASTOS DEDUCIBLES\n"))
otros_gastos = float(input(f"# C)OTROS GASTOS NO DEDUCIBLES\n"))

gastos_totales = float(gastos_deducibles + otros_gastos)

base_imponible = abs(float((gastos_totales) - ingresos_totales))

impuesto_pagar = abs(float(base_imponible * 10 / 100))  # Por una regla de tres.

print(f"#########################################################################################")
print(f"#                          -FORMULARIO ABONO TRIMESTRAL-                                #")
print(f"#                                                                                       #")
print(f"# TITULAR...........{nombre}                 GASTOS DEDUCIBLES.{ gastos_deducibles:.2f}€  ") 
print(f"#                                                                                       #")
print(f"#                                            OTROS GASTOS......{ otros_gastos:.2f}€       ")
print(f"#                                                                                       #")
print(f"# INGRESOS TOTALES..{ingresos_totales:.2f}                  GASTOS TOTALES....{ gastos_totales:.2f}€    ")
print(f"#                                                                                       #")
print(f"#                     BASE IMPONIBLE.......{base_imponible:.2f}€                         ")
print(f"#                                                                                       #")
print(f"#                      TOTAL A ABONAR......{impuesto_pagar:.2f}€                         ")
print(f"#                                                                                       #")
print(f"#########################################################################################")