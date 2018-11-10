
class NodoArbol:

    def __init__(self,nodoPadre,Estado,profundidad,costoCamino,f):
        self.estado = Estado
        self.nodoPadre = nodoPadre
        if self.nodoPadre == None:
            self.costoCamino = 0 
            self.accion = 'Estoy en la raiz'
            self.profundidad = 0
        else:
            self.costoCamino=nodoPadre.costoCamino+costoCamino #Actualizado a CostoCamino del nodoActual 
            self.accion="Estuve en "+nodoPadre.estado.nodoActual+" y ahora estoy en "+self.estado.nodoActual
            self.profundidad=nodoPadre.profundidad+1
        self.f = f

