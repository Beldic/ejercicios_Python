# Ejercicio 21 - Registro de gastos y ahorros
# Autor: Jordi Casado
# Versión: 1.0

"""
    Crea un programa en Python que simule el registro de gastos y ahorros. Utiliza variables para
    representar el saldo inicial, solicita al usuario ingresar gastos y ahorros, y utiliza operadores
    y el método append() para actualizar la información. Realiza las siguientes operaciones:

    1. Pregunta al usuario por su saldo inicial utilizando input().

    2. Muestra un mensaje de bienvenida y un saldo inicial. 

    3. Pregunta al usuario por el importe de un gasto y lo resta al saldo. 

    4. Pregunta al usuario por el importe de un ahorro y lo suma al saldo. 

    5. Muestra el saldo actualizado y una lista con los gastos y ahorros registrados. 

"""

saldo_actual = []

saldo_actual.append(float(input(" \n Hola, introduce tu saldo inicial: ")))

print (f" \n Bienvenid@, tu SALDO INICIAL es: {saldo_actual[0]} €")

saldo_actual.append(float(input(" \n Introduce el importe de tu GASTO (-): ")))

saldo_actual.append(saldo_actual[0] - saldo_actual[1])

saldo_actual.append(float(input(" \n Introduce el importe de tu AHORRO (+): ")))

saldo_actual.append(saldo_actual[2] + saldo_actual[3])

print(f" \n SALDO ACTUAL : {saldo_actual[4]} € \n\n Lista con los registros de gastos y ahorros actualizados: \n {saldo_actual} € \n")

