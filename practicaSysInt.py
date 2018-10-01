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
	def adyacentesNodo(self,osmid_node):
		nodosAdyacentes=[]
		_arista=[]
		for arista in self.graph.edges():
			if osmid_node in arista:
				nodosAdyacentes.append()
		return nodosAdyacentes
		
osmid = "847673135"
file="Migueltura.graphml"
g=grafo(file)
print(g.perteneceNodo(osmid))
print(g.posicionNodo(osmid))
'''print(g.adyacentesNodo(osmid))'''








