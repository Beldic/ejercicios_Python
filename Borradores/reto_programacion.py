

# CORRECCIÓN EJERCICIO 4 (GRUPO3)--------------------------------------------------------------------------------------------
# CÓDIGO TESTEADO

numero_entero = 10

numero_decimal = 3.14

cadena = "Hola mundo"

booleano = True

print("Tipo de dato de numero_entero:", type(numero_entero))

print("Tipo de dato de numero_decimal:", type(numero_decimal))

print("Tipo de dato de cadena:", type(cadena))

print("Tipo de dato de booleano:", type(booleano))

nombre = input("Por favor, ingresa tu nombre: ")

nombre_mayusculas = nombre.upper()

nombre_minusculas = nombre.lower()

print("Nombre en mayúsculas:", nombre_mayusculas)

print("Nombre en minúsculas:", nombre_minusculas)

num1 = float(input("Ingresa el primer número: "))

num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2

resta = num1 - num2

multiplicacion = num1 * num2

division = num1 / num2

print("Suma:", suma)

print("Resta:", resta)

print("Multiplicación:", multiplicacion)

print("División:", division)

resultado = num1 + (num2 * num2) / num1

print("Resultado:", resultado)

lista = [1, 2, 3, 4, 5]

tupla = (1, 2, 3, 4, 5)

conjunto = {1, 2, 3, 4, 5}

diccionario = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e':'5'}

print("Lista:", lista)

print("Tupla:", tupla)

print("Conjunto:", conjunto)

print("Diccionario:", diccionario)

notas_estudiantes = {

"Juan": "8",

"María": "9",

"Pedro": "7",

"Ana": "6",

"Luis": "5"

}

nota_juan = int(input("Introduce la nota de juan: "))

nota_juan = notas_estudiantes.update({"Juan": nota_juan})

nota_maria = int(input("Introduce la nota de Maria: "))

nota_maria = notas_estudiantes.update({"Maria": nota_maria})

nota_pedro = int(input("Introduce la nota de pedro: "))

nota_pedro = notas_estudiantes.update({"Pedro": nota_pedro})

nota_ana = int(input("Introduce la nota de ana: "))

nota_ana = notas_estudiantes.update({"Juan": nota_ana})

nota_luis = int((input("Introduce la nota de luis: ")))

nota_luis = notas_estudiantes.update({"Luis": nota_luis})

print(notas_estudiantes)

print("Notas de los estudiantes: ")

print(notas_estudiantes)

print("Diccionario:", diccionario)

#----------------------------------------------------------------------------------------------------------------------------------------
