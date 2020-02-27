class Palabras:
    def __init__(self, words):
        self.palabras = words
    
    def getPalabras(self):
        return self.palabras

    def getUnion(self, conjunto):
        union = set(self.getPalabras())|set(conjunto.getPalabras()); #union de conjuntos.
        return sorted(union)
    def diferenciaConjuntos(self, words):
        conjuntoA = []
        conjuntoB = []
        for i in range(1,len(words)):
            if (words[i] != '{' and words[i]!= '}'):
                if(words[i] != ','):
                    conjuntoA.append(words[i])
            else:
                print('hola')
        return conjuntoA
