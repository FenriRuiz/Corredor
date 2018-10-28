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
        for nodo in self.listaPendientes:
            h.update(nodo.encode())
        return h.hexdigest()

class EspacioEstados:
    def __init__(self,file):
        self.graph=Grafo(file)
        self.listaEstados=[]
    def sucesores(self, Estado):
        nodosAdy = self.graph.adyacentesNodo(Estado.nodoActual)
        for nodoAdy in nodosAdy:    
            #Hay que hacer funcion recursiva que llame a Sucesores y pille los adyacentes del nodo de estado y los añada
            #a listaEstados
            accion = "Estoy en " + nodoAdy['nInicial'] + " y voy a "+ nodoAdy['nFinal']
            coste = nodoAdy['length']
            #Obtenemos el coste y el nodo al que vamos de la arista
            sucesion=(accion,Estado(nodoAdy['nFinal']),coste)
            self.listaEstados.append(sucesion)
    def esta(self,estado):
        return estado in self.listaEstados

    
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
    def __init__(self, Estado, NodoArbol=0):
        self.estado = Estado
        if NodoArbol == 0:
            self.costoCamino = 0 
            self.accion = 'Estoy en la raiz'
            self.profundidad = 0
        else:
            self.costoCamino = NodoArbol.costoCamino # +  
            self.accion = ''#Acción del ¿espacio de estados?
            self.profundidad = NodoArbol.profundidad # +
        self.f = Estado.nodoActual

class Frontera:
    def __init__(self, orden='idNodo'):
        self.frontera = []
        self.orderBy = orden
    def insert(self, NodoArbol, frontera):
        frontera.append(NodoArbol)
        if self.orderBy == 'profundidad':
            sorted(frontera, key = lambda NodoArbol: NodoArbol[3])
        elif self.orderBy == 'coste':
            sorted(frontera, key = lambda NodoArbol: NodoArbol[1])
        else: # Frontera.orderBy == 'idNodo'
            sorted(frontera, key = lambda NodoArbol: NodoArbol[0])

    def delete(self, frontera):
        if(not frontera.isEmpty):
            return frontera.pop(0)
        else:
            return 0
    def isEmpty(self, frontera):
        if(not frontera):
            return True
        else:
            return False


'''data = open("fichero.json", "r")
datos = data.read()
data_string = json.loads(datos)
Problema(data_string)'''

data=open("fichero.json","r")
datos=data.read()
problema=json.loads(datos)

es=Estado(problema['IntSt']['nodes'], problema['IntSt']['listNodes'])
print(es.nodoActual) 



