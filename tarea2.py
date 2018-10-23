import networkx as nx 
import hashlib
import json
class Estado:
    def __init__(self,nodoOSM):
        self.nodoActual=nodoOSM['node']
        self.nodosPendientes=nodoOSM['listNodes']
        self.identificador=self.serializar()
    def serializar(self):
        h = hashlib.md5() 
        h.update(self.nodoActual.encode())
        for nodo in self.nodosPendientes:
            h.update(nodo.encode())
        return h.hexdigest()
# data=open("fichero.json","r")
# datos=data.read()
# problema=json.loads(datos)

# es=estado(problema['IntSt'])
# print('')
class EspacioEstados:
    graph=nx.Graph()
    sucesiones=[]
    def __init__(self,file):
        self.graph=nx.read_graphml(file)
    def Sucesores(self,estado):
        for nodoDestino in estado.nodosPendientes:
            accion="Estoy en "+estado.identificador+" y voy a "+nodoDestino
            sucesion=(accion,estado(nodoDestino),1)
            #Hace falta calcular el coste
            self.sucesiones.append(sucesion)
    def esta(self,estado):
        return estado in self.sucesiones

    
class Problema:
    def __init__(self,json):
        self.espacioEstados=EspacioEstados(json['graphlmfile'])
        self.estadoInicial=Estado(json['IntSt'])
    def esObjetivo(self,estado):
        if(not estado.nodosPendientes):
            return True
        else:
            return False
# class NodoArbol:
#     def __init__(self,espacioEstados):
#         estado=espacioEstados.sucesiones[0]




