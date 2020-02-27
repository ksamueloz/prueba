curse = "estudien"
string = "curso de codigo facilito prros jajaja"

#Metodos de formato
result = '{} de {}'.format(string, curse) #esto ayuda a concatenar
print(result)
result = '{a} de {b}'.format(a = string, b = curse) #es lo mismo de arriba pero otra forma de escribirlo
print(result)

result = result.lower() # cambia todo a minuscula
print(result)

result = result.upper() # convierte todo a mayuscula
print(result)

result = result.title() # pone el string como un titulo
print(result)


#Metodos de busqueda

pos = result.find('Codigo') #devuelve la posicion de la palabra especifica en la cadena
print(pos)

count = result.count('i') # devuelve la cantidad de veces que se repite
print(count)

nuevo = result.replace('C', 'x')# ayuda a reemplazar valores del string por un dato especifico
print(nuevo)

nuevo = result.split(' ') # divide el string  cuando encuentra un simbolo de corte especificado
print(nuevo)