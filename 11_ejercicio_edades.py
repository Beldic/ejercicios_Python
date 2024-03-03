#Ejercicio11: Programa de calculadora de edades. 
#Autor: Jordi Casado.
#versión: 1.0

"""
 Crea un programa en Python que solicite al usuario ingresar su año de nacimiento y el año actual. 
 Utiliza esta información para calcular su edad actual y edad futura. 

 1. Solicita al usuario que introduzca su año de nacimiento. 
 2. Solicita al usuario que introduzca su año actual. 

 Luego, realiza los siguientes cálculos. 

 * Calcula la edad actual restando el año de nacimiento y el año actual. 
 * Calcula la edad que tendría en 5 años sumando 5 a la edad actual. 
 * Calcula la edad que tendría en 10 años sumando 10 a la edad actual. 

"""

print("\n¡BIENVENIDO A LA CALCULADORA DE EDADES!\n")

nacimiento = int(input("\nIntroduce tu año de nacimiento: "));
actual = int(input("\nIntroduce el año actual: "));

edad = actual - nacimiento

print(f" Tienes {edad} años, ¡Aún te quedan muchas cosas buenas por vivir! \n En cinco años tendras {edad + 5} años. \n En diez años tendrás {edad + 10} años.\n")


