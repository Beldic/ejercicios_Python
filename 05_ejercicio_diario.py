

# Ejercicio 5: programa que simule un gestor de información de un diario.
# Autor: Jordi Casado
# Versión: 1.0

"""Crea un programa que simule un gestor de información de un diario. 
Para ello el programa deberá solicitar al usuario que introduzca la fecha con formato DÍA DE LA SEMAMA + día del mes(en número)
 + mes. Además en una nueva instrucción le pedirá al usuario que introduzca la hora y en una nueva instrucción 
 le pedirá el texto de la entrada que desea almacenar. Al finalizar el programa mostrará al usuario toda la información 
 con el siguiente formato: 

• fecha string en mayúscula 

• hora string

• texto de la entrada del diario en minúscula"""

print("\n ### TE DAMOS LA BIENVENIDA A TU DIARIO ### \n")

dia_semana = str(input("\n *Introduce el dia de la semana: "))  #Día de la semana en string con salto de línea
dia_mes = int(input("\n *Introduce el día del mes (número): "))          #Día del mes en tipo entero con salto de línea 
mes = str(input("\n *Introduce el mes correspondiente: "))      #Mes en tipo string con salto de línea

fecha = dia_semana +"/"+str(dia_mes)+"/"+mes+"\n" # Concatenamos los datos para tenerlos en una única cadena. 

hora_aproximada = str(input("\n *Introduce la hora aproximada :")) #Hora en formato string con salto de línea

texto = str(input("\n *Introduce el texto de tu entrada:\n")).lower() #Texto introducido por el usuario y convertido a minúsculas.

print("\n *DIARIO* \nFECHA:"+fecha.upper()+"HORA:"+hora_aproximada+"\nTEXTO:"+texto.lower()+"\n")    #Imprime los datos introducidos anteriormente.