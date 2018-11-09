import hashlib


class Estado:
    def __init__(self,nodoActual, nodosPendientes):
        self.nodoActual=nodoActual #nodoOSM['node']
        self.nodosPendientes=nodosPendientes #nodoOSM['listNodes']
        #self.identificador=self.serializar()
    def serializar(self):
        h = hashlib.md5() 
        h.update(self.nodoActual.encode())
        for nodo in self.nodosPendientes:
            h.update(nodo.encode())
        return h.hexdigest()


class NodoArbol:
    #A diferencia de java, no podemos poner varios constructores pero si valores por defecto.
    def __init__(self,nodoPadre,Estado,profundidad,costoCamino,f):
        self.estado = Estado
        self.nodoPadre = nodoPadre
        if nodoPadre == None:
            self.costoCamino = 0 
            self.accion = 'Estoy en la raiz'
            self.profundidad = 0
        else:
            self.costoCamino=nodoPadre.costoCamino+costoCamino #Actualizado a CostoCamino del nodoActual 
            self.accion="Estuve en "+str(nodoPadre.estado.nodoActual)+" y ahora estoy en "+str(self.estado.nodoActual)
            self.profundidad=nodoPadre.profundidad+1
        self.f = f
class Frontera:
    frontera=[]
    def crea(self):
        self.frontera=sort())
    def insert(self, NodoArbol):
        self.frontera.append(NodoArbol)
        self.crea()

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

e1=Estado(1,[2,3])
e2=Estado(2,[3])
e3=Estado(3,[])

n1=NodoArbol(None,e1,0,0,e1.nodoActual)
n2=NodoArbol(n1,e2,1,1,e2.nodoActual)
n3=NodoArbol(n2,e3,2,2,e3.nodoActual)

frontera=Frontera()
frontera.crea()
frontera.insert(n1)
frontera.insert(n3)
frontera.insert(n2)



print('123')




