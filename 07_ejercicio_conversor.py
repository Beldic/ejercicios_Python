
#Ejercicio7: Conversor de temperatura (Celsius - Fahrenheit).
#Autor: Jordi Casado
#Version: 1.0


"""Crea un programa en Python que solicite al usuario introducir la temperatura en grados Celsius. 
Luego, realiza la conversión de esta temperatura a grados Fahrenheit utilizando la fórmula:

F=9/5⋅C+32
G=5/9*F-32

Donde *F* es la temperatura en grados Fahrenheit y *C* es la temperatura en grados Celsius.

Finalmente, muestra el resultado de la temperatura en ambas escalas. 
Utiliza f-strings para formatear la salida y muestra la temperatura en grados Fahrenheit con dos decimales."""

temperatura = float(input("\nIntroduce un número en grados Celsius: \n")) # Pedir al usuario que introduzca una temperatura en grados Celsius
resultado_f = float(9 / 5 * temperatura + 32)

print(f"\n La temperatura en grados Celsius {temperatura} es {resultado_f} en grados fahrenheit")

temperatura2 = float(input("\nIntroduce un número en grados Fahrenheit \n")) #Pedir al usuario que introduzca  una temperatura en grados fahrenheit
resultado_g = float(5 / 9 * (temperatura2 - 32))

print(f"\n La temperatura en grados Fahrenheit {temperatura2} es {resultado_g} \n")

