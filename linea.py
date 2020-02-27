import sys
from comandos import Palabras

words = sys.argv[1:]
llave = Palabras(words)
llave.getPalabras()
print(llave.getPalabras())


print('prueba')
cona = Palabras(words)
conb = Palabras(words)
cona.diferenciaConjuntos(words)