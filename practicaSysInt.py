import networkx as nx 

class grafo():
	graph=nx.Graph()
	nodes=None
	def __init__(self,file):
		self.graph=nx.read_graphml(file)
		self.nodes=nx.get_node_attributes(self.graph,'osmid')
	def perteneceNodo(self,osmid_node):
		return osmid_node in self.nodes
	def posicionNodo(self,osmid_node):
		if(self.perteneceNodo(osmid_node)):
			posicion=[]
			posicion.append(self.graph._node[osmid_node])
			return posicion
		else:
			return "Error, el nodo no existe"
osmid = "847673135"
file="Migueltura.graphml"
g=grafo(file)
print(g.perteneceNodo(osmid))
print(g.posicionNodo(osmid))








