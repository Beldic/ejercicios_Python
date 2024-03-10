# Ejercicio - COMPRA EN FRUTERIA 
# Autor: Jordi Casado 
# Versión: 1.0
# Tema del ejercicio: Creamos una tabla de listas anidadas con el tipo de fruta y su precio el kilo. A continuación creamos una lista cesta de la compra 
# para simular una compra de fruta en base a un presupuesto dado. Si nos pasamos del presupuesto nos avisa. Al terminar la compra nos muestra 
# el cambio o presupuesto restante.  

# Al principio creamos una tabla con listas anidadas para frutas y sus precios por kilo. 

tabla_precios_fruta = [

    [ "manzana",  1.2 ],  # Primera fila: Tipo de fruta y precio por kilo 
    [ "pera",    0.8 ],   # Segunda fila
    [ "platano", 0.95 ],  # Tercera fila 
    [ "kiwi",    1.3 ],   # Cuarta fila  
    [ "fresa",   0.75 ]   # Quinta fila

]

print(f"\n -BIENVENID@ A LA FRUTERIA PYTHON-")

# Imprimir la tabla de frutas y precios
print("\nTabla de Frutas y Precios por Kilo:")
print("------------------------------------")
print("Fruta\t\tPrecio por Kilo (€)")
print("------------------------------------")
for fruta, precio in tabla_precios_fruta:
    
    print(f"{fruta}\t\t{precio}")

# Solicitar al comprador que ingrese los datos de su cesta de la compra. 

cesta_compra = []

fruta = input(f"\nIngresa el tipo de fruta que deseas comprar (o escribe 'final' para terminar): ")

while fruta != "final":
    kilos = float(input(f"\nIngrese la cantidad en kilos de {fruta}: "))
    cesta_compra.append([fruta, kilos])
    fruta = input(f"\nIngresa el tipo de fruta que deseas comprar (o escribe 'final' para terminar): ")

# Solicitar al usuario que ingrese su presupuesto
    
presupuesto = float(input("Ingresa tu presupuesto en euros: "))


# Calcular el precio total de la compra y restar del presupuesto. 
    
for fruta, kilos, in cesta_compra:

    for fruta_tabla, precio in  tabla_precios_fruta:

        if fruta == fruta_tabla:

            precio_fruta = kilos * precio

            if precio_fruta <= presupuesto:

                presupuesto -= precio_fruta 

                print(f"Has comprado {kilos} kilos de {fruta} por {precio_fruta:.2f} €. Tu presupuesto restante es: {presupuesto:.2f} €")

            else:

                print(f"No tienes suficiente presupuesto para comprar {kilos} kilos de {fruta}. Tu presupuesto restante: {presupuesto:.2f} €")
                      
            break # Salir del bucle interno cada vez que se encuentre la fruta


# Imprimir el presupuesto restante
        
print(f"¡Gracias por la compra! Tu presupuesto restante es: {presupuesto:.2f} €")



 















