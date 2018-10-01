import networkx as nx 

class arista():
	nodo_inicial=None
	nodo_final=None
	nombre=None
	longitud=None

class grafo():
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
	def adyacentesNodo(self,osmid_node):
		listaAristas=[]
		if(self.perteneceNodo(osmid_node)):
			for edge in self.graph.edges._adjdict[osmid_node]:
				a=arista()
				arista.nodo_inicial=osmid_node
				arista.nodo_final=edge
				arista.nombre=self.graph.edges._adjdict[osmid_node][edge][0]['name']
				arista.longitud=self.graph.edges._adjdict[osmid_node][edge][0]['length']
				listaAristas.append(a)
		else:
			return "Error, el nodo no existe"
		return listaAristas


osmid = "1128335617"
file="Migueltura.graphml"
g=grafo(file)
print(g.perteneceNodo(osmid))
print(g.posicionNodo(osmid))
print(g.adyacentesNodo(osmid))








