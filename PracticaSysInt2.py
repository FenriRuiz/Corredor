import networkx as nx 
import hashlib
import json
import sys

class Estado():
    def __init__(self, osmid_node, listaFrontera, idCode):
        self.nodo = osmid_node
        self.frontera = listaFrontera
        self.serial = self.codeGenerator(osmid_node, listaFrontera)
    def codeGenerator(self, osmid_node, listaFrontera):
        h = hashlib.new(osmid_node)
        h.update(listaFrontera)
        h.hexdigest()
        return h

class EspacioEstados():
    def __init__(self, file):
        self.graph= nx.read_graphml(file)
        self.nodes = self.graph.node
    def sucesores(self, Estado):
        accM = "Estoy en " + Estado.nodo + " y voy  a " + Estado.listaFrontera
        costeAcci = Estado.listaFrontera
    def esta(self, osmid_node):
        return osmid_node in self.nodes
class Problema():
    def __init__(self, EspacioEstados):
        self.EspacioEstados = EspacioEstados
    def estadoInicial(self, filejson):
        json
class Frontera():
    def __init__(self, listaFrontera):
        ''' Crea la lista frontera vacía y establece el criterio de ordenación '''
        self.listaFrontera = []
