import networkx as nx 
import hashlib
import json
##
##TAREA 1
class Grafo():
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
	def adyacentesNodo(self,nodo_inicial):
		listaAristas=[]
		if(self.perteneceNodo(nodo_inicial)):
			for nodo_final in self.graph.edges._adjdict[nodo_inicial]:
				try:
					nombre= self.graph.edges._adjdict[nodo_inicial][nodo_final][0]['name']
				except KeyError:
					nombre='SinNombre'
				arista=({'nInicial' : nodo_inicial,'nFinal' : nodo_final, 'nombre' : nombre, 
				'longitud' : self.graph.edges._adjdict[nodo_inicial][nodo_final][0]['length']})
				listaAristas.append(arista)
				'''Cambiar el name y ver si podemos devolverlo como una cuadrupleta'''
		else:
			print("Error, el nodo no existe")
			return listaAristas
		return listaAristas

class Estado:
    def __init__(self,nodoActual, nodosPendientes):
        self.nodoActual=nodoActual #nodoOSM['node']
        self.nodosPendientes=nodosPendientes #nodoOSM['listNodes']
        self.identificador=self.serializar()
    def serializar(self):
        h = hashlib.md5() 
        h.update(self.nodoActual.encode())
        for nodo in self.nodosPendientes:
            h.update(nodo.encode())
        return h.hexdigest()

class EspacioEstados:
    def __init__(self,file):
        self.graph=Grafo(file)
    def sucesores(self, Estado):
        nodosAdy = self.graph.adyacentesNodo(Estado.nodoActual)
        listaEstados=[]
        for nodoAdy in nodosAdy:    
            #Hay que hacer funcion recursiva que llame a Sucesores y pille los adyacentes del nodo de estado y los añada
            #a listaEstados
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

    
class Problema:
    def __init__(self,json):
        self.espacioEstados=EspacioEstados(json['graphlmfile'])
        self.estadoInicial=Estado(json['IntSt']['node'], json['IntSt']['listNodes'])
    def esObjetivo(self, Estado):
        if(not Estado.listaPendientes):
            return True
        else:
            return False

class NodoArbol:
    #A diferencia de java, no podemos poner varios constructores pero si valores por defecto.
    def __init__(self,nodoPadre,Estado,profundidad,costoCamino,f):
        self.estado = Estado
        self.nodoPadre = nodoPadre
        if nodoPadre == None:
            self.costoCamino = 0 
            self.accion = 'Estoy en la raiz'
            self.profundidad = 0
        else:
            self.costoCamino=nodoPadre.costoCamino+costoCamino #Actualizado a CostoCamino del nodoActual 
            self.accion="Estuve en "+nodoPadre.estado.nodoActual+" y ahora estoy en "+self.estado.nodoActual
            self.profundidad=nodoPadre.profundidad+1
        self.f = f

class Frontera:
    def __init__(self):
        self.frontera = []
    def insert(self, NodoArbol):
        self.frontera.append(NodoArbol)
        #sorted(frontera, key = lambda NodoArbol: NodoArbol[4])

    def delete(self):
        if(not self.isEmpty()):
            return self.frontera.pop(0)
        else:
            return 0
    def isEmpty(self):
        if(not self.frontera):
            return True
        else:
            return False

def creaListaNodosArbol(listaEstados,nodoActual,profMax,estrategia):
    #something
    return ""
def creaSolucion(nodoActual):
    '''La solución es:
    Estrategia:uniforme
    Total Nodos Generados:1888
    Profundidad:36
    costo:10871.6
    Esto podría ser lo de creaSolucion'''
    return ""

def busquedaAcotada(prob,estrategia,profMax):
    #No estoy seguro si se inicializan aquí todas las cosillas
    frontera=Frontera()
    nodoInicial=NodoArbol(None,prob.estadoInicial,0,0,0)
    frontera.insert(nodoInicial)
    solucion=False

    while solucion==False and not frontera.isEmpty():
        nodoActual=frontera.delete()
        if(prob.esObjetivo(nodoActual.estado)):
            solucion=True
        else:
            listaEstados=prob.espacioEstados.sucesores(nodoActual.estado)
            listaNodos=creaListaNodosArbol(listaEstados,nodoActual,profMax,estrategia) #Metodo que crea nodos arboles por la lista de estados
            frontera.insert(listaNodos) #Llamo a insert porque a un array le daría igual insertar un objeto que un array de objetos
    if (solucion==True):
        return creaSolucion(nodoActual)
    else :
        return "Sin solucion"


def busqueda(prob,estrategia,profMax,incProf):
    profActual=incProf
    Solucion=""
    while not Solucion and profActual <= profMax:
        Solucion=busquedaAcotada(prob,estrategia,profActual)
        profActual=profActual+incProf
    return Solucion


data=open("fichero.json","r")
datos=data.read()
prob=Problema(json.loads(datos))


    
 
#main()


