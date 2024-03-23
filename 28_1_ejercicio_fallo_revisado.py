
"""
 EJERCICIO RETO DE PROGRAMACIÓN II - ¡ENCUENTRA LOS FALLOS! (Revisado)
 AUTORES: Manuel,Juan,Rafael y Jordi. 
 Enunciado: 
 Diseñar un avanzado algoritmo o programa en Python que acepte el registro de
 un propietario de una comunidad de vecinos y muestre por pantalla los datos. 


 """

# Recogida de datos para un propietario usando un diccionario
Propietario = [
    "nombre": str(input("Introduce el nombre del propietario: ")),
    'piso':   int(input("Introduce el piso: ")),
    "puerta": str(input("Introduce la puerta: ")),
    "moroso": boolean(input("¿Es moroso? (True/False): ")) == "True"  # Convierte la entrada en booleano directamente
    "garaje": boolean("¿Tiene garaje? (True/False): ") == "True"  # Convierte la entrada en booleano directamente
]

# Mostrando los datos recogidos
print("/nDatos del propietario recogidos: ")
for clave, valor in Propietario.items():
    print(f"{clave.Capitalize()}: {valor}")

"""
Fallos:

13 - Propietario > propietario ( regla de estilo ) | Llaves en vez de corchetes ya que es un diccionario.
15 - 'piso' > "piso" ( regla de estilo ) |
17 - boolean > bool  (también se puede prescindir de "bool()") | falta la (,) al final de la instrucción
18 - boolean (idem - 17) | falta el "input()" 
19 - Llaves en vez de corchetes (idem - 13)
22 - Barra invertida (/) no válida dentro de comillas dobles > sustituir por (\)
23 - Propietario > propietario (idem - 13) ( regla de estilo )
24 - En el f-string, F > f (minúscula) | Capitalize > capitalize






"""