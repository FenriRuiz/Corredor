import networkx as nx 
import json
import os

from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema

def creaListaNodosArbol(listaEstados,nodoActual,profMax,estrategia):
    list = []
    
    for est in listaEstados:
        p = nodoActual.profundidad+1
        c = nodoActual.costoCamino + est.nodoActual['length']
        f = -(nodoActual.profundidad+1)
        nodoNuevo = NodoArbol(nodoActual, est, p, c, f)
        list.append(nodoNuevo)

    return list
def creaSolucion(nodoActual):
    '''La solución es:
    Estrategia:uniforme
    Total Nodos Generados:1888
    Profundidad:36
    costo:10871.6
    Esto podría ser lo de creaSolucion'''
    return ""

def busquedaAcotada(prob,estrategia,profMax):
    frontera=Frontera()
    nodoInicial=NodoArbol(None,prob.estadoInicial,0,0,0)
    frontera.insert(nodoInicial, 0)
    solucion=False

    while solucion==False and not frontera.isEmpty():
        nodoActual=frontera.delete()
        if(prob.esObjetivo(nodoActual.estado)):
            solucion=True
        else:
            listaEstados = prob.espacioEstados.sucesores(nodoActual.estado)
            listaNodos= creaListaNodosArbol(listaEstados,nodoActual,profMax,estrategia) #Metodo que crea nodos arboles por la lista de estados

            for n in listaNodos:
                frontera.insert(n, n.f)
            # frontera.insert(listaNodos) #Llamo a insert porque a un array le daría igual insertar un objeto que un array de objetos
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

    opcionMenu = input("")
    if opcionMenu == "1":
        estrategia = opcionMenu
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,estrategia,profMax,incProf)
    elif opcionMenu == "2":
        estrategia = opcionMenu
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,estrategia,profMax,incProf)
    elif opcionMenu == "3":
        estrategia = opcionMenu
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,estrategia,profMax,incProf)
    elif opcionMenu == "4":
        estrategia = opcionMenu
        print("Digame la profundidad máxima")
        profMax = input("")
        print("Digame la incremento en la profundidad")
        incProf = input("")
    elif opcionMenu == "5":
        estrategia = opcionMenu
        print("Digame la profundidad máxima")
        profMax = input("")
        incProf = 1
        busqueda(prob,estrategia,profMax,incProf)