from Estado import Estado
from Grafo import Grafo

class EspacioEstados:
    def __init__(self,file):
        self.graph=Grafo(file)
    
    def sucesores(self, estado):
        nodosAdy = self.graph.adyacentesNodo(estado.nodoActual)
        listaEstados=[]
        for nodoAdy in nodosAdy:    
            listaPendientes=estado.listaPendientes
            accion = "Estoy en " + nodoAdy['nInicial'] + " y voy a "+ nodoAdy['nFinal']+" via:"+nodoAdy['nombre']
            coste = nodoAdy['longitud']
            if nodoAdy['nFinal'] in estado.listaPendientes:
                listaPendientes.remove(nodoAdy['nFinal'])
               # print(listaPendientes)   
            #Obtenemos el coste y el nodo al que vamos de la arista
            print(accion)
            
            estadoNuevo=Estado(nodoAdy['nFinal'],listaPendientes)
            sucesion=(accion,estadoNuevo,coste)
            listaEstados.append(sucesion)
        return listaEstados
    
    def esta(self,estado):
        return self.graph.perteneceNodo(estado.nodoActual)
