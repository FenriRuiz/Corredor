import networkx as nx 
import json
import os
import time

from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema

BFS = 1
DFS = 2
DFS_IT = 3
COST = 4
VORAZ=5
A=6


def calcularF(estrategia,coste,profundidad,nodoActual):
    if(estrategia==DFS):
        return float(-profundidad)
    elif(estrategia==BFS):
        return float(profundidad)
    elif(estrategia==COST):
        return coste
    elif(estrategia==VORAZ):
        return nodoActual.estado.heuristica(nodoActual.estado) #this is not correct, (node1,node2) node1 suposed to be nodoActual
    elif(estrategia==A):
        #no clue about dis
        print('')
 

def creaListaNodosArbol(listaSucesiones,nodoActual,profMax,estrategia):
    listNodosArbol=[]
    for sucesion in listaSucesiones:
        profundidad = nodoActual.profundidad+1
        coste = float(nodoActual.costoCamino) + float(sucesion[2])
        f = calcularF(estrategia,coste, profundidad,nodoActual)
        
        nodoNuevo = NodoArbol(nodoActual, sucesion[1], profundidad, coste, f)
        
        listNodosArbol.append(nodoNuevo)
    
    return listNodosArbol
def recorreNodoPadre(nodo):
    if(nodo != None):
        recorreNodoPadre(nodo.nodoPadre)
        print('\n'+nodo.accion)
        print(nodo.estado.listaPendientes)

def creaSolucion(nodoActual,numNodos):
    recorreNodoPadre(nodoActual)
    print('Nodos generados-->'+str(numNodos))
    print('Profundidad-->'+str(nodoActual.profundidad))
    print('Costo-->'+str(nodoActual.costoCamino))  
    return True

def busquedaAcotada(prob,estrategia,profMax):
    frontera=Frontera()
    nodoInicial=NodoArbol(None,prob.estadoInicial,0,0,0)
    listVisitados=[]
    frontera.insert(nodoInicial)
    solucion=False

    while (solucion==False) and (not frontera.isEmpty()):
        nodoActual=frontera.delete()
        listVisitados.append((nodoActual.estado.identificador,nodoActual.f))
        if(prob.esObjetivo(nodoActual.estado)):
            solucion=True
        else:
            listaSucesiones = prob.espacioEstados.sucesores(nodoActual.estado)
            listaNodos= creaListaNodosArbol(listaSucesiones,nodoActual,profMax,estrategia) #Metodo que crea nodos arboles por la lista de estados
            for n in listaNodos:
                if (not(any((n.estado.identificador== nodoRecorrido[0] or (n.f < nodoRecorrido[1])  for nodoRecorrido in listVisitados)))):
                    frontera.insert(n)
    if (solucion==True):
        return creaSolucion(nodoActual,len(listVisitados))
    else :
        return None

def busquedaInformada(prob,estrategia,profMax):
    frontera=Frontera()
    nodoInicial=NodoArbol(None,prob.estadoInicial,0,0,0)
    listVisitados=[]
    frontera.insert(nodoInicial)
    solucion=False

    while (solucion==False) and (not frontera.isEmpty()):
        nodoActual=frontera.delete()
        listVisitados.append((nodoActual.estado.identificador,nodoActual.f))
        if(prob.esObjetivo(nodoActual.estado)):
            solucion=True
        else:
            listaSucesiones = prob.espacioEstados.sucesores(nodoActual.estado)
            listaNodos= creaListaNodosArbol(listaSucesiones,nodoActual,profMax,estrategia) #Metodo que crea nodos arboles por la lista de estados
            for n in listaNodos:
                if (not(any((n.estado.identificador== nodoRecorrido[0] or (n.f < nodoRecorrido[1])  for nodoRecorrido in listVisitados)))):
                    frontera.insert(n)
    if (solucion==True):
        return creaSolucion(nodoActual,len(listVisitados))
    else :
        return None


def busqueda(prob,estrategia,profMax,incProf):
    profActual=incProf
    Solucion=False
    while Solucion==False and (profActual <= profMax):
        Solucion=busquedaAcotada(prob,estrategia,profActual)
        profActual=profActual+incProf
    return Solucion

def menu():
    #os.system('clear')
    print("Seleccione la estrategia de búsqueda a usar")
    print("\t 1 - Busqueda en ANCHURA")
    print("\t 2 - Busqueda en PROFUNDIDAD SIMPLE")
    print("\t 3 - Busqueda en PROFUNDIDAD ITERATIVA")
    print("\t 4 - Busqueda por COSTE")
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
        profMax = int(input(""))
        incProf = 1
        ts=time.time()
        busqueda(prob,BFS,profMax,incProf)
        print('Estrategia--> Anchura')
        tf=time.time()
        print(tf-ts)
    elif opcionMenu == DFS:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1
        ts=time.time()
        busqueda(prob,DFS,profMax,incProf)
        tf=time.time()
        print('Estrategia--> Profundidad')
        print(tf-ts)
    elif opcionMenu == DFS_IT:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        print("Digame la incremento en la profundidad")
        incProf = input("")
        #busqueda(prob,DFS_IT,profMax,incProf)
        print('Estrategia--> Profundidad Iterativa')
    elif opcionMenu == COST:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1
        ts=time.time()
        busqueda(prob,COST,profMax,incProf)
        tf=time.time()
        print('Estrategia--> Coste')
        print(tf-ts)