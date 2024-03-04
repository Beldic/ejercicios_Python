#Ejercicio 14: Evalúa las condiciones. 
#Autor: Jordi Casado
#Versión : 1.0
"""
Crea un programa en Python que simule la evaluación de condiciones utilizando operadores lógicos. 
Situaciones:
1.Un estudiante ha aprobado si su puntuación es mayor o igual a 60.
2.Un usuario tiene acceso si es un administrador o tiene una suscripción premium. 
3.Un número es positivo si es mayor que 0 y menor que 100.
4.Un equipo gana si ha anotado más de 3 goles y no ha recibido ningún gol en contra. 

Nota: he empleado aparte de los operadores lógicos (AND OR o NOT) las sentencias de control (IF-ELSE).

"""


print("\n - EJERCIDIO DE OPERADORES LÓGICOS -  ")


puntuacion = int(input("\n Introduce tu puntuación "))

if(puntuacion >=  60):

    print("\n El estudiante ha aprobado ")

else:

    print("\n El estudiante no ha aprobado")


administrador = int(input("\n Si eres administrador introduce 1 : \n"))
acceso = int(input("\n Si tienes una suscripción premiun introduce 1 : \n"))

if ( (administrador == 1) or (acceso == 1)):

    print("\nAcceso permitido");



else:
    print("\n Acceso denegado ");



numero = int(input("\n  Ingrese un número entero"))

if ( numero > 0 and numero < 100):

    print("El número es positivo entre 0 y 100")


goles_anotados = int(input("\n Introduce los goles anotados" ))
goles_recibidos = int(input("\n Introduce los goles recibidos"))



if ((goles_anotados > 2) and (goles_recibidos == 0)):

    print("\n ¡¡¡El equipo ha ganado!!!")

else:

    print("\n ¡¡¡El equipo ha perdido!!!")




