# Ejercicio 43 - Calculadora básica con while
# Autor: Jordi Casado
# Versión: 1.0

"""
ENUNCIADO:

Desarrolla un programa en Python que simule una calculadora básica. El programa solicitará al usuario que ingrese dos números y luego le permitirá realizar operaciones matemáticas básicas seleccionando un operador. El programa continuará ejecutándose hasta que el usuario decida salir.

1. El programa iniciará un bucle **`while`** para permitir la ejecución continua del programa.
2. Dentro del bucle, el programa solicitará al usuario que ingrese dos números y almacenará estos valores en variables.
3. Luego, el programa solicitará al usuario que seleccione un operador matemático entre suma (+), resta (-), multiplicación (*) o división (/).
4. Dependiendo del operador seleccionado, el programa realizará la operación correspondiente con los dos números ingresados.
5. El resultado de la operación se mostrará al usuario.
6. Después de mostrar el resultado, el programa preguntará al usuario si desea continuar o salir del programa.
7. Si el usuario elige continuar, el programa volverá al paso 2.
8. Si el usuario elige salir, el programa imprimirá un mensaje de despedida y finalizará la ejecución.

"""


estado_ON = True     #Creo un estado ON de la calculadora que comienza en True



while estado_ON == True:      # Mientras el estado sea True, se ejecutara el bucle while. 

    arranque = str(input("Introduce el valor de ON o OFF de la calculadora: ").upper()) # Creo una variable arranque ON, OFF 

    if arranque == "ON":  # Si el usuario escribe "ON" activa la calculadora 

        estado_ON = True

        operacion = str(input("Introduce la operación aritmética para operar: SUMA, RESTA, PRODUCTO O DIVISION: ").upper()) # variable operación

        valor_1 = float(input("Introduzca el primer valor: "))   # Introduce los valores a operar 
        valor_2 = float(input("Introduzca el segundo valor: "))

        if operacion == "SUMA":        # Suma de dos numeros

            res = valor_1 + valor_2  

            

        elif operacion == "RESTA":        # Resta de dos numeros

            res = valor_1 - valor_2

            

        elif operacion == "PRODUCTO":        # Multiplicación de dos numeros

            res = valor_1 * valor_2

            

        elif operacion == "DIVISION":         # División entre dos numeros

            if (valor_2) == 0: 

                print  ("Error, no se puede dividir entre cero")

                res = None

            else:
            
                res = valor_1 / valor_2

            

            

        print(res) # Imprime el resultado de la opeación seleccionada 

    elif arranque == "OFF":  # Salida del programa

        estado_ON = False   # Se cambia a False para indicar que el sistema esta apagado

        print("Fin de la aplicación")


