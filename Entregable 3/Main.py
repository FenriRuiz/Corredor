import networkx as nx 
import json

from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema

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
print("MENU")
