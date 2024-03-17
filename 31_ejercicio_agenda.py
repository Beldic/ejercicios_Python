# Ejercicio 31 - Agenda Telefónica
# Aut@r: Jordi Casado
# Versión: 1.0
"""
ENUNCIADO:

1. Crea un diccionario llamado **`agenda_telefonica`** que contenga los nombres de algunas personas como claves y sus números de teléfono como valores.
2. Imprime el diccionario completo para verificar su contenido.
3. Accede al número de teléfono de una persona específica en la agenda telefónica e imprímelo.
4. Añade una nueva entrada a la agenda telefónica para una persona adicional junto con su número de teléfono.
5. Modifica el número de teléfono de una persona existente en la agenda telefónica.
6. Elimina una entrada de la agenda telefónica para una persona que ya no necesita ser contactada.
7. Imprime el diccionario actualizado para verificar los cambios realizados.




"""

agenda_telefonica = {

    "Pepe" : "7947356975",
    "Noelia": "8210947310",
    "Juanito": "7946356975",  
    "Maria": "3784957394"
}
print(f"\n -AGENDA TELEFONICA-  ")
print(agenda_telefonica)


contacto = agenda_telefonica["Juanito"] # Acceder al contacto. 

print(f"\n el numero de Juanito es: {contacto} \n")


agenda_telefonica["Lucía"] = "9876543210" # Añadir un nuevo contacto a la agenda.

print(f"\n {agenda_telefonica}")

agenda_telefonica["Pepe"] = "00560485068"

print(f"\n Nuevo telefono del usuario Pepe: {agenda_telefonica['Pepe']}\n")

del agenda_telefonica["Noelia"] # Eliminar un contacto de la agenda.

print("\nContactos despues de eliminar 'Noelia':\n ",agenda_telefonica)