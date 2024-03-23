diccionario = {'a': 1, 'b': 2, 'c': 3}

valor = diccionario.get('a')

print (valor)

diccionario2 = { 'c' : 4 , 'd' : 5 }

diccionario.update(diccionario2)

print (diccionario)

valor2 = diccionario2.update(c=5,  d=6)

print(valor2)

valor_setdefault = diccionario.setdefault('g',20)


print(valor_setdefault)

valor_setdefault_dos = diccionario2.setdefault('h',10)

print(valor_setdefault_dos)
