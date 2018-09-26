import networkx as nx 

class grafo():
	graph=nx.Graph()
	nodes=None
	def __init__(self,file):
		self.graph=nx.read_graphml(file)
		self.nodes=nx.get_node_attributes(self.graph,'osmid')
	def perteneceNodo(self,osmid_node):
		for id,osmid in self.nodes.items():
			if osmid == osmid_node:
				return True
		return False

osmid = "847673135"
file="Migueltura.graphml"
g=grafo(file)
print(g.perteneceNodo(osmid))







