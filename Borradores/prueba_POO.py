
"""

class Asteroide:

    def posicion(self,posX: int,posY: int):

        self.posX = posX
        self.posY = posY

        return(f"La posición del asteroide es: {posX} : {posY}")







asteroide1 = Asteroide()

asteroide1.posicion(100,50)

print(asteroide1.posicion(100,50))

"""

class Persona: 

    def __init__(self, nombre:str, edad:int, color_piel:str, profesion:str, estado_civil:str ):

        self.nombre = nombre
        self.edad = edad
        self.color_piel = color_piel
        self.profesion = profesion
        self.estado_civil = estado_civil

    def
        

    
# Hay que crear una función para imprimir el objeto o hacer un return???

    




pepe = Persona("Pepe", 25, "blanco", "abogado", "soltero")
antonia = Persona("Antonia", 18, "blanca", "estudiante","soltera")


print(vars(pepe))   #No se pude imprimir por pantalla un objeto de forma directa? 
print(vars(antonia))

