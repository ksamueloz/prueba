diccionario = {'a':55, 'e':True, 'a':100}# las claves deben de ser inmutables
#si una llave se repite siempre toma la ultima
print(diccionario)

diccionario2 = {'a':55, 'e':True, 'a':100}
diccionario2['c']="nuevo string" #agregar un nuevo dato nombre[clave]=string/int/etc
diccionario2['a']= False # si la llave se encuentra la actualiza y si no la crea
print(diccionario2)

valor = diccionario2['a'] #obtener un valor de un diccionario
print(valor)

valor = diccionario2.get('e', False) #otra forma de buscar un valor diccionario.get(clave a buscar, valor a devolver si no lo encuentra)
print(valor)

del diccionario2['e'] # Nos ayuda a eliminar un valor del diccionario
print(diccionario2)

llaves = diccionario2.keys() #Regresa todas las llaves del diccionario
print(llaves)

llaves = list(diccionario2.keys()) # Devuelve todas las llaves y las agrega a una lista
print(llaves)

valores = diccionario2.values() # Devuelve todos los valores del diccionario
print(valores)

valores = list(diccionario2.values()) # Devuleves todos los valores en forma de listas
print(valores)

llaves = tuple(diccionario2.keys()) # Devuelve todas las llaves en forma de tuplas
valores = tuple(diccionario2.values()) # Devuelve todos los valores en forma de tuplas
print(llaves , valores)

diccionario3 = {'z':23, 'w':88}
"""diccionario2['z'] = diccionario3['z']# esto es una forma de extender un diccionario
diccionario2['w'] = diccionario3['w']"""


diccionario2.update(diccionario3) # Esta es una forma optimizada de como extender diccionarios
print(diccionario2)