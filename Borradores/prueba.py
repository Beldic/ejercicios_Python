


"""

tupla = (1,2,3,["hola","adios"])

print(tupla.append("otra vez"))

"""
ventas_enero = {

    'mouse' : 10,
    'teclados' : 50
}

productos_vendidos = 0

for producto in ventas_enero.values():

    productos_vendidos += producto

print(productos_vendidos)

productos_vendidos = 0


for clave in ventas_enero.keys():

    productos_vendidos += ventas_enero[clave]


print(productos_vendidos)