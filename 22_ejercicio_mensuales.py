# Ejercicio 22 - Registro de gastos mensuales
# Autor: Jordi Casado
# Versión: 1.0

"""
Vamos a crear un programa en Python que te permita llevar un registro de tus gastos 
mensuales en diferentes categorías. Utilizaremos un bucle for para iterar a través de
las categorias de gastos y solicitar al usuario que ingrese los importes correspondientes.
Al final, elprograma calculará y mostrará el total de gastos. 

1. Cre una lista llamada categorías_gastos  que contenga las siguientes categorías:
   "Alimentación","Trasnporte","Entretenimiento","Servicios" y "Otros".

2. Inicializa una variable llamada total_gastos, en 0 para acumular el total de gastos. 

3. Utiliza el bucle for para iterar a través de las categorías de los gastos. Dentro del
   bucle:
    - Solicita al usuario que eingrese el importe de gasto para cada categoría. 
    - Convierte la entrada del usuario a tipo float. 
    - Acumula el importe total de gastos. 
4. Muestra un resumen de gastos mensuales por categoría utilizando otro bucle for
5. Finalmente, muestra el total de gastos mensuales. 

"""





categoria_gastos =["Alimentación","Transporte","Entretenimiento","Servicios","Otros"]

total_gastos = 0



for indice in categoria_gastos:
        

             
        

            importe_gasto = float(input(f"\n Introduce el importe de {indice} : "))

            
        
            total_gastos += importe_gasto

            print(f"\n Gasto en {indice} : {importe_gasto} € \n")
    
            

    
            print(f" Gasto Total Acumulado: {total_gastos} € \n")

             


print(f" Total de gastos mensuales: {total_gastos} € \n")