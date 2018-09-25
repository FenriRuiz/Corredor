import networkx as nx 
'''FUNCIONES :)'''
def perteneceNodo(osmidnodo):
	for id, osmid in nodosEx.items():
		if osmid == osmidnodo:
			return True
	return False

'''CREACION DEL GRAFO Y POBLACIÓN DEL MISMO'''
g = nx.Graph()

g= nx.read_graphml("Migueltura.graphml")

''' OBTENEMOS LOS NODOS EXISTENTES'''
nodosEx = nx.get_node_attributes(g, 'osmid')

'''EJEMPLO OSMID EXISTENTE: 847673135''' 
osmid = "847673135"
print(perteneceNodo(osmid))


