import networkx as nx 
'''FUNCIONES :)'''
def perteneceNodo(osmidnodo):
	for id, osmid in nodosOsmid.items():
		if osmid == osmidnodo:
			return True
	return False
def posicionNodo(osmidnodo):
	if perteneceNodo(osmidnodo):
		for id, x in nodosLat.items():
			pos[0] = float(x)
		for id, y in nodosLon.items():
			pos[1] = float(y)
		return pos
	else:
		raise ValueError("No existe el nodo seleccionado")

def adyacentesNodo(osmidnodo):
	it = nx.all_neighbors(g, osmid)
	aristas = edges_iter()
	return it

'''CREACION DEL GRAFO Y POBLACIÓN DEL MISMO'''
g = nx.Graph()

g= nx.read_graphml("Migueltura.graphml")

''' OBTENEMOS LOS NODOS EXISTENTES'''
nodosOsmid = nx.get_node_attributes(g, 'osmid')
nodosLat = nx.get_node_attributes(g, 'x')
nodosLon = nx.get_node_attributes(g, 'y')

'''EJEMPLO OSMID EXISTENTE: 847673135''' 
osmid = "847673135"
print(perteneceNodo(osmid))
pos=[0,0]
print(posicionNodo(osmid))
adyacentesNodo(osmid)