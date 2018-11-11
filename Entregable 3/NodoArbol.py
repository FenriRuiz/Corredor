
class NodoArbol:

    def __init__(self,nodoPadre,Estado,profundidad,costoCamino,f):
        self.estado = Estado
        self.nodoPadre = nodoPadre
        if self.nodoPadre == None:
            self.costoCamino = 0 
            self.accion = 'Estoy en la raiz'
            self.profundidad = 0
        else:
            self.costoCamino=costoCamino #Actualizado a CostoCamino del nodoActual 
            self.profundidad=profundidad
            self.accion=""+nodoPadre.estado.nodoActual+"->"+self.estado.nodoActual+" |"+str(self.nodoPadre.costoCamino)+" "+str(self.profundidad)+" "+str(self.costoCamino)+" |"
 
        self.f = f
        #print(self.accion)

