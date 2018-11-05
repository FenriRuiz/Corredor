import networkx as nx 
import hashlib
import json
##
##TAREA 1
class Grafo():
	graph=nx.Graph()
	nodes=None
	def __init__(self,file):
		self.graph=nx.read_graphml(file)
		self.nodes=self.graph._node
	def perteneceNodo(self,osmid_node):
		return osmid_node in self.nodes
	def posicionNodo(self,osmid_node):
		if(self.perteneceNodo(osmid_node)):
			posicion=[]
			posicion.append(self.nodes[osmid_node])
			return posicion
		else:
			return "Error, el nodo no existe"
	def adyacentesNodo(self,nodo_inicial):
		listaAristas=[]
		if(self.perteneceNodo(nodo_inicial)):
			for nodo_final in self.graph.edges._adjdict[nodo_inicial]:
				try:
					nombre= self.graph.edges._adjdict[nodo_inicial][nodo_final][0]['name']
				except KeyError:
					nombre='SinNombre'
				arista=({'nInicial' : nodo_inicial,'nFinal' : nodo_final, 'nombre' : nombre, 
				'longitud' : self.graph.edges._adjdict[nodo_inicial][nodo_final][0]['length']})
				listaAristas.append(arista)
				'''Cambiar el name y ver si podemos devolverlo como una cuadrupleta'''
		else:
			print("Error, el nodo no existe")
			return listaAristas
		return listaAristas

class Estado:
    def __init__(self,nodoActual, nodosPendientes):
        self.nodoActual=nodoActual #nodoOSM['node']
        self.nodosPendientes=nodosPendientes #nodoOSM['listNodes']
        self.identificador=self.serializar()
    def serializar(self):
        h = hashlib.md5() 
        h.update(self.nodoActual.encode())
        for nodo in self.nodosPendientes:
            h.update(nodo.encode())
        return h.hexdigest()

class EspacioEstados:
    def __init__(self,file):
        self.graph=Grafo(file)
    def sucesores(self, Estado):
        nodosAdy = self.graph.adyacentesNodo(Estado.nodoActual)
        listaEstados=[]
        for nodoAdy in nodosAdy:    
            #Hay que hacer funcion recursiva que llame a Sucesores y pille los adyacentes del nodo de estado y los añada
            #a listaEstados
            listaPendientes=Estado.nodosPendientes
            accion = "Estoy en " + nodoAdy['nInicial'] + " y voy a "+ nodoAdy['nFinal']+" via:"+nodoAdy['nombre ']
            coste = nodoAdy['length']
            if nodoAdy in Estado.nodosPendientes:
                listaPendientes.remove(nodoAdy)
            #Obtenemos el coste y el nodo al que vamos de la arista
            sucesion=(accion,Estado(nodoAdy['nFinal'], listaPendientes),coste)
            listaEstados.append(sucesion)
        return listaEstados
    def esta(self,estado):
        return self.graph.perteneceNodo(estado.nodoActual)

    
class Problema:
    def __init__(self,json):
        self.espacioEstados=EspacioEstados(json['graphlmfile'])
        self.estadoInicial=Estado(json['IntSt']['node'], json['IntSt']['listNodes'])
    def esObjetivo(self, Estado):
        if(not Estado.listaPendientes):
            return True
        else:
            return False

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
            self.costoCamino=nodoPadre.costoCamino+espacioBusqueda[2]
            self.accion="Estuve en "+nodoPadre.estado.nodoActual+" y ahora estoy en "+self.estado.nodoActual
            self.profundidad=nodoPadre.profundidad+1
        self.f = f

class Frontera:
    def __init__(self):
        self.frontera = []
    def insert(self, NodoArbol):
        frontera.append(NodoArbol)
        #sorted(frontera, key = lambda NodoArbol: NodoArbol[4])

    def delete(self):
        if(not self.frontera.isEmpty):
            return frontera.pop(0)
        else:
            return 0
    def isEmpty(self):
        if(not self.frontera):
            return True
        else:
            return False

class Busqueda:
    self.prob=Problema("fichero.json")
    def __init__(self):
        self.frontera=Frontera()
        self.nInicial=NodoArbol(None,prob.estadoInicial,0,0,0)
        self-frontera.insert(self.nInicial)
        self.solucion=False
    def busquedaAcotada(self,prob,estrategia,profMax):
        while not self.solucion and not self.frontera.isEmpty():
            nActual=self.frontera.delete()
            if(prob.esObjetivo(nActual.estado)):
                self.solucion=True
            else:
                listaEstados=prob.espacioEstados.sucesores(nActual.estado)
                listaNodos=CreaListaNodosArbol #What is dis



'''data = open("fichero.json", "r")
datos = data.read()
data_string = json.loads(datos)
Problema(data_string)'''
def main():
    data=open("fichero.json","r")
    datos=data.read()
    prob=Problema(json.loads(datos))

    # def __init__(self,json):
    # self.espacioEstados=EspacioEstados(json['graphlmfile'])
    # self.estadoInicial=Estado(json['IntSt']['node'], json['IntSt']['listNodes'])
    print(prob.estadoInicial.nodoActual)
 
main()


