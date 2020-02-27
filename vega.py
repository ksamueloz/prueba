import sys
from conjuntos import  Conjunto
obtenerValores = sys.argv[1:]

#print(obtenerValores);
#modo de escritura.
#{conjunto1}.{conjunto2}
#hol

conjuntos = obtenerValores[0].split("}.{");

conjunto1 = Conjunto(["1","2","6","4"],4);
conjunto2 = Conjunto(["3","2","5","7"],4);

print(conjunto1.getUnion(conjunto2))


#print(conjuntos)


"""@andres te toca."""
def separarConjuntos(conjuntos):
    for i in range(len(conjuntos)):
        conjuntos[i] = conjuntos[i].replace("{", "")
        conjuntos[i] = conjuntos[i].replace("}", "")
    return conjuntos

a = separarConjuntos(conjuntos)
print(conjuntos)