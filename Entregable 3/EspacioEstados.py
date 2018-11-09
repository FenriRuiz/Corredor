from Estado import Estado
from Grafo import Grafo

class EspacioEstados:
    def __init__(self,file):
        self.graph=Grafo(file)
    
    def sucesores(self, Estado):
        nodosAdy = self.graph.adyacentesNodo(Estado.nodoActual)
        listaEstados=[]
        for nodoAdy in nodosAdy:    ç
            listaPendientes=Estado.nodosPendientes
            accion = "Estoy en " + nodoAdy['nInicial'] + " y voy a "+ nodoAdy['nFinal']+" via:"+nodoAdy['nombre ']
            coste = nodoAdy['length']
            if nodoAdy in Estado.nodosPendientes:
                listaPendientes.remove(nodoAdy)
            #Obtenemos el coste y el nodo al que vamos de la arista
            sucesion=(accion,Estado(nodoAdy['nFinal'], listaPendientes),coste)
            listaEstados.append(sucesion)
        return listaEstados
    
    def esta(self,estado):
        return self.graph.perteneceNodo(estado.nodoActual)
