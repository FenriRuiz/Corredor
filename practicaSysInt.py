import networkx as nx 

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
	def adyacentesNodo(self,nodo_inicial):
		listaAristas=[]
		if(self.perteneceNodo(nodo_inicial)):
			for nodo_final in self.graph.edges._adjdict[nodo_inicial]:
				arista=[nodo_inicial,
				nodo_final,
				self.graph.edges._adjdict[nodo_inicial][nodo_final][0]['name'],
				self.graph.edges._adjdict[nodo_inicial][nodo_final][0]['length']]
				listaAristas.append(arista)
		else:
			return "Error, el nodo no existe"
		return listaAristas


osmid = "1128335617"
file="Migueltura.graphml"
g=grafo(file)
print(g.perteneceNodo(osmid))
print(g.posicionNodo(osmid))
print(g.adyacentesNodo(osmid))










