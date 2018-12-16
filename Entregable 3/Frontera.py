class Frontera:
    def __init__(self):
        self.frontera = []

    def insert(self, NodoArbol):
        i = 0
        for hoja in self.frontera:
            if hoja.estado.identificador == NodoArbol.estado.identificador:
                self.frontera.pop(i)
            i=i+1
        self.frontera.append(NodoArbol)
        self.frontera.sort(key = lambda x: x.f)

    def delete(self):
        if(not self.isEmpty()):
            return self.frontera.pop(0)
        else:
            return 0

    def isEmpty(self):
        if(not self.frontera):
            return True
        else:
            return False
