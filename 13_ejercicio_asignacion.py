#Ejercicio13 Actualización de la puntuación(operadores de asignación)
#Autor: Jordi Casado
#Versión 1.0

""" Crea un programa en Python que simule la actualización de la puntuación de un juego. 
Inicializa una variable llamada puntuación con un valor inicial de 100. Luego, utiliza 
operadores de asignación para realizar las siguientes acciones:

1. Incrementa la puntuación en 10 unidades: Ha adquirido una vida extra
2. Reduce la puntuación en 5 unidades: Ha sido alcanzado por un enemigo
3. Multiplica la puntuación por 2: Ha recibido un bonus extra
4. Divide la puntuación por 4: Ha repartido el botín entre el equipo
5. Calcula el módulo de la puntuación entre 3: Ha perdido la parte del botín 
no repartida de forma equitativa entre los miembros del equipo. 

Muestra la puntuación después de cada operación utilizando la función print(). 



"""

print("\n ¡ACTUALIZANDO TU PUNTUACIÓN!")


puntuacion = 100;
print(f"\n Puntuación inicial: {puntuacion}  - Es tu puntuación inicial.")
puntuacion += 10
print(f"\n Puntuación después de incrementar: {puntuacion} - Ha adquirido vida extra.")
puntuacion -= 5
print(f"\n Puntuación después de reducir: {puntuacion} - Ha sido alcanzado por un enemigo.")
puntuacion *= 2
print(f"\n Puntuación después de multiplicar por 2: {puntuacion} - Ha recibido un bonus .")
puntuacion /= 4
print(f"\n Puntación después de dividir por 4: {puntuacion} - Ha repartido el botín entre el equipo.")
puntuacion %= 3
print(f"\n Puntación después de calcular el módulo entre 3: {puntuacion} - Ha perdido parte del botín no repartida de forma equitativa entre los miembros del equipo.")

