class Conjunto:

    def __init__(self,array,cantElementos):
        self.elementos = array;
        self.cantElementos = cantElementos;

    def __str__(self):
        elementos = "{";
        for i in range(self.cantElementos):
            elementos += str(self.elementos[i]) + ", " if (i < self.cantElementos -1) else str(self.elementos[i]) + "}";
            print(i)
        return elementos;

    def getCantElementos(self):
        return self.cantElementos;

    def getElementos(self):
        return self.elementos;

    def setElementos(self,newArrayElementos):
        self.elementos = set(self.elementos)|set(newArrayElementos); #union de conjuntos.

    def getUnion(self,conjuntoOBJ):
        union = set(self.getElementos())|set(conjuntoOBJ.getElementos()); #union de conjuntos.
        return sorted(union)