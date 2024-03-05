#Ejercicio 16 - Gestión de usuarios (operadores de pertenencia & identidad)
#Autor: Jordi Casado. 
#Versión: 1.0

""" 
Crea un programa en Python que simule la gestión de usuarios en un sistema. 
Utiliza variables para representar información sobre dos usuarios diferentes. 
Luego,utiliza operadores de pertenencia (in, not in) y de identidad (is, is not)
para realizar las siguientes acciones:

1. Verifica si un usuario llamado usuario_actual está registrado en el sistema. 
2. Comprueba si ambos usuarios comparten la misma dirección de correo_electrónico.
3. Identifica si los objetos que representan a los usuarios son diferentes. 
4. Muestra los resultados utilizando la función print().

"""





print("\n Bienvenido al Sistema de Gestión del Sistema \n")


user_1 = str(input(" nombre del primer usuario: "))
mail_1 = str(input(" introduce tu eMail: "))

user_2 = str(input(" nombre del segundo usuario: "))
mail_2 = str(input(" introduce tu eMail: "))


users = [ "admin", user_2] # Lista con los nombres de las listas. 

print(f"\nRegistro de usuario {user_1} = { user_1 in users} \n")

print(f"Comprobación del correo electrónico: { mail_1 is mail_2 }\n")

print(f"Los usuarios {user_1} y {user_2} son diferentes: {user_1 is not user_2} ")

