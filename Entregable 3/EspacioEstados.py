from Estado import Estado
from Grafo import Grafo

class EspacioEstados:
    def __init__(self, file):
        self.graph=Grafo(file)
    
    def sucesores(self, estado):
        nodosAdy = self.graph.adyacentesNodo(estado.nodoActual)
        listaEstados=[]
        
        for nodoAdy in nodosAdy:
            listaPendientes=[]
            for p in estado.listaPendientes:
                listaPendientes.append(p)
            #listaPendientes=estado.listaPendientes
            accion = "Estoy en " + nodoAdy['nInicial'] + " y voy a "+ nodoAdy['nFinal']+" via:"+nodoAdy['nombre']
            coste = nodoAdy['longitud']
            if nodoAdy['nFinal'] in estado.listaPendientes:
                listaPendientes.remove(nodoAdy['nFinal'])
            estadoNuevo=Estado(nodoAdy['nFinal'],listaPendientes)
            sucesion=(accion,estadoNuevo,coste)
            listaEstados.append(sucesion)
        return listaEstados
    def lonlat(self, idnode):
        return (float(self.graph.nodes[idnode]['x']),float(self.graph.nodes[idnode]['y']))
    
    def esta(self, estado):
        return self.graph.perteneceNodo(estado.nodoActual)
