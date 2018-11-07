class Frontera:
    def __init__(self):
        self.frontera = []
    def insert(self, NodoArbol):
        self.frontera.append(NodoArbol)
        #sorted(frontera, key = lambda NodoArbol: NodoArbol[4])

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
