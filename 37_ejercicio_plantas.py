# Ejercicio 37 - Enciclopedia de plantas
# Autor: Jordi Casado 
# Versión: 1.0

"""

ENUNCIADO:

1. Define un diccionario llamado **`enciclopedia_plantas`** que contenga información sobre diferentes plantas. Cada planta será representada por un diccionario anidado con las siguientes claves: "nombre", "especie", "familia", "origen", "altura" y "usos". Puedes agregar al menos 3 plantas con esta estructura.
2. Crea una lista llamada **`nombres_plantas`** que contenga los nombres de todas las plantas presentes en la enciclopedia.
3. Agrega una nueva planta a la enciclopedia. Para ello, solicita al usuario que ingrese los detalles de la nueva planta y agrégalos al diccionario principal **`enciclopedia_plantas`**.
4. Imprime la información de todas las plantas de la enciclopedia. Recorre la lista de nombres de plantas (**`nombres_plantas`**) y utiliza cada nombre para acceder al diccionario correspondiente en **`enciclopedia_plantas`** y mostrar toda la información de la planta.
5. Finalmente, muestra el número total de plantas presentes en la enciclopedia. Utiliza la función **`len()`** para determinar la longitud de la lista de nombres de plantas.

"""


enciclopedia_plantas = {
    "Rosa": {
        "nombre": "Rosa",
        "especie": "Rosa spp.",
        "familia": "Rosaceae",
        "origen": "Asia",
        "altura": "Varía entre 0.5 y 2 metros",
        "usos": "Ornamental, medicinal, perfumería, gastronomía"
    },
    "Lavanda": {
        "nombre": "Lavanda",
        "especie": "Lavandula angustifolia",
        "familia": "Lamiaceae",
        "origen": "Mediterráneo",
        "altura": "0.6 a 1 metro",
        "usos": "Ornamental, aceites esenciales, relajante"
    },
    "Aloe Vera": {
        "nombre": "Aloe Vera",
        "especie": "Aloe barbadensis miller",
        "familia": "Asphodelaceae",
        "origen": "Península Arábiga",
        "altura": "0.5 a 1 metro",
        "usos": "Medicinal, cosmético, alimenticio"
    }
}



for planta in enciclopedia_plantas:     #2    

    nombre_plantas = enciclopedia_plantas[planta]["nombre"]

    print(nombre_plantas)


# Solicitar al usuario que ingrese los detalles de la nueva planta
nombre = input("Ingresa el nombre de la planta: ")
especie = input("Ingresa la especie de la planta: ")
familia = input("Ingresa la familia de la planta: ")
origen = input("Ingresa el origen de la planta: ")
altura = input("Ingresa la altura promedio de la planta: ")
usos = input("Ingresa los usos principales de la planta: ")

# Actualizar el diccionario principal con la nueva planta
enciclopedia_plantas[nombre] = {
    "nombre": nombre,
    "especie": especie,
    "familia": familia,
    "origen": origen,
    "altura": altura,
    "usos": usos
}

for planta in enciclopedia_plantas:    # Recorro el diccionario  para mostrarlo por pantalla

    for clave, valor in  enciclopedia_plantas[planta].items():

        print(f"\n{clave}: {valor}")



total_plantas =  len(enciclopedia_plantas)   # Número total de plantas

print("\n", total_plantas)