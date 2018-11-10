import networkx as nx 
import json
import os

from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema

BFS = 1
DFS = 2
DFS_AC = 3
DFS_IT = 4
COST = 5

def calcularF(estrategia,coste,profundidad):
    if(estrategia==DFS):
        return -profundidad
    elif(estrategia==BFS):
        return profundidad
    elif(estrategia==COST):
        return coste

def creaListaNodosArbol(listaSucesiones,nodoActual,profMax,estrategia):
    listNodosArbol=[]
    for sucesion in listaSucesiones:
        profundidad = nodoActual.profundidad+1
        coste = float(nodoActual.costoCamino) + float(sucesion[2])
        f = calcularF(estrategia,coste, profundidad)
        
        nodoNuevo = NodoArbol(nodoActual, sucesion[1], profundidad, coste, f)
        
        listNodosArbol.append(nodoNuevo)
    
    return listNodosArbol
def creaSolucion(nodoActual):
    '''La solución es:
    Estrategia:uniforme
    Total Nodos Generados:1888
    Profundidad:36
    costo:10871.6
    Esto podría ser lo de creaSolucion'''
    print('polla')
    return ""

def busquedaAcotada(prob,estrategia,profMax):
    frontera=Frontera()
    nodoInicial=NodoArbol(None,prob.estadoInicial,0,0,0)
    listCaminoNodos=[]
    frontera.insert(nodoInicial)
    listCaminoNodos.append(nodoInicial)
    solucion=False
    contNodos=0

    while solucion==False or not frontera.isEmpty():
        nodoActual=frontera.delete()
        if(prob.esObjetivo(nodoActual.estado)):
            solucion=True
        else:
            listaSucesiones = prob.espacioEstados.sucesores(nodoActual.estado)
            listaNodos= creaListaNodosArbol(listaSucesiones,nodoActual,profMax,estrategia) #Metodo que crea nodos arboles por la lista de estados
            contNodos=contNodos+listaNodos.__len__()
            print(contNodos)
            for n in listaNodos:
                frontera.insert(n)
                    # else:
                    #     if(n.f < nodo.f):
                    #         frontera.frontera.remove(nodo)
                    #         listCaminoNodos.remove(nodo)
                    #         frontera.insert(n)
                    #         listCaminoNodos.append(n)
                # if(not (n.estado.nodoActual in listCaminoNodos)):
                #     frontera.insert(n)
                #     listCaminoNodos.append(n)
                # else:
                #     for  nodo in listCaminoNodos:
                #         if(n.f < nodo.f):
                #             frontera.frontera.remove(n)
                #             listCaminoNodos.remove(n)
                #             frontera.insert(n)
                #             listCaminoNodos.append(n)
                        
                

            
            # frontera.insert(listaNodos) #Llamo a insert porque a un array le daría igual insertar un objeto que un array de objetos
    if (solucion==True):
        return creaSolucion(nodoActual)
    else :
        return None


def busqueda(prob,estrategia,profMax,incProf):
    profActual=incProf
    Solucion=None
    while Solucion==None or (profActual <= profMax):
        Solucion=busquedaAcotada(prob,estrategia,profActual)
        profActual=profActual+incProf
    return Solucion

def menu():
    os.system('cls')
    print("Seleccione la estrategia de búsqueda a usar")
    print("\t 1 - Busqueda en ANCHURA")
    print("\t 2 - Busqueda en PROFUNDIDAD SIMPLE")
    print("\t 3 - Busqueda en PROFUNDIDAD ACOTADA")
    print("\t 4 - Busqueda en PROFUNDIDAD ITERATIVA")
    print("\t 5 - Busqueda por COSTE")
    print("\t 9 - Salir")


data=open("fichero.json","r")
datos=data.read()
prob=Problema(json.loads(datos))
print("MENU")
while True:
    menu()

    opcionMenu = int(input(""))
    if opcionMenu == BFS:
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,BFS,profMax,incProf)
    elif opcionMenu == DFS:
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,DFS,profMax,incProf)
    elif opcionMenu == DFS_AC:
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        #busqueda(prob,DFS_AC,profMax,incProf)
    elif opcionMenu == DFS_IT:
        print("Digame la profundidad máxima")
        profMax = input("")
        print("Digame la incremento en la profundidad")
        incProf = input("")
        #busqueda(prob,DFS_IT,profMax,incProf)
    elif opcionMenu == COST:
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,COST,profMax,incProf)