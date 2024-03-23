# Ejercicio 32 - Agenda Telefónica 2
# Autor: Jordi Casado
# Versión: 1.0

"""
ENUNCIADO:

1. Crea un diccionario llamado **`agenda_telefonica`** que contenga al menos cinco contactos, donde cada contacto tenga un nombre como clave y un número de teléfono como valor.
2. Utiliza el método **`clear()`** para eliminar todos los elementos del diccionario y verifica que ahora está vacío.
3. Utiliza el método **`update()`** para agregar nuevos contactos a la agenda. Puedes agregar múltiples contactos al mismo tiempo proporcionando un diccionario adicional con los nuevos contactos.
4. Utiliza el método **`copy()`** para crear una copia del diccionario original y verifica que la copia es independiente del original.
5. Utiliza el método **`get()`** para obtener el número de teléfono de un contacto existente y de un contacto inexistente. Asegúrate de proporcionar un valor predeterminado para el caso en que el contacto no exista.
6. Utiliza el método **`pop()`** para eliminar un contacto de la agenda y devolver su número de teléfono. Verifica que el contacto ya no está en la agenda y que el método devuelve el valor correcto.
7. Utiliza el método **`popitem()`** para eliminar el último contacto añadido a la agenda y verifica que el método devuelve una tupla con el contacto eliminado.
8. Utiliza el método **`keys()`** para obtener una lista de todas las claves en la agenda.
9. Utiliza el método **`values()`** para obtener una lista de todos los valores en la agenda.
10. Utiliza el método **`items()`** para obtener una lista de tuplas, donde cada tupla contiene una clave y su valor correspondiente en la agenda.
11. Utiliza el método **`setdefault()`**  para comprobar si tenemos apuntado el teléfono de tu profesora, y si no está apuntado, que lo incluya en tu diccionario.













"""

agenda_telefonica = {

    "Paco" : "912345678",
    "Maria": "654789012",
    "Juanito": "123456789",
    "Lucas": "555555555",
    "Pepita": "999999999"
}

print(agenda_telefonica)

agenda_telefonica.update(Manoli = "432234344")

print(agenda_telefonica)

agenda_copia = agenda_telefonica.copy()

print(agenda_copia)

contacto_existente = agenda_telefonica.get("Maria")
contacto_inexistente = agenda_telefonica.get("Bartolo")

print( contacto_existente, contacto_inexistente)

valor_eliminado = agenda_telefonica.pop("Paco")

print( valor_eliminado)

ultimo_valor_eliminado = agenda_telefonica.popitem() 

print( ultimo_valor_eliminado )

lista_de_claves = agenda_telefonica.keys()

print (lista_de_claves)

lista_de_valores = agenda_telefonica.values()

print (lista_de_valores)

items_de_la_agenda = agenda_telefonica.items()

print (items_de_la_agenda)

setdefault_agenda = agenda_telefonica.setdefault ("María", "123456789")

print( setdefault_agenda)

agenda_telefonica.clear()

print(agenda_telefonica)