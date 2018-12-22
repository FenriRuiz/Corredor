import json
import time

from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema

BFS = 1
DFS = 2
DFS_IT = 3
COST = 4
VORAZ = 5
A = 6
def heuristica(nodoActual, nSucesor):
    minimoaPendiente = []
    for pendiente in nodoActual.estado.listaPendientes:
        minimoaPendiente.append(prob.distance(pendiente, nSucesor))
    return min(minimoaPendiente)
def calcularF(estrategia, coste, profundidad,nSucesor , nodoActual):

    if estrategia == DFS:
        return -(profundidad)
    elif estrategia == BFS:
        return float(profundidad)
    elif estrategia == COST:
        return -(coste)
    elif estrategia == VORAZ:
        return round(heuristica(nodoActual, nSucesor),1)
    elif estrategia == A:
        return round(prob.distance(nodoActual.estado.nodoActual, nSucesor) + coste,1)
        #round(coste + heuristica(nodoActual, nSucesor),1)

def creaListaNodosArbol(listaSucesiones, nodoActual, profMax, estrategia):
    listNodosArbol = []
    for sucesion in listaSucesiones:
        profundidad = nodoActual.profundidad + 1
        if profundidad <= profMax:
            coste = round(float(sucesion[2]) + float(nodoActual.costoCamino),1)

            f = calcularF(estrategia, coste, profundidad, sucesion[1].nodoActual, nodoActual)

            nodoNuevo = NodoArbol(nodoActual, sucesion[1], profundidad, coste, f)
            listNodosArbol.append(nodoNuevo)

    return listNodosArbol

def recorreNodoPadre(nodo):
    costePares = 0
    if nodo != None:
        costePares = recorreNodoPadre(nodo.nodoPadre)
        if (int(nodo.estado.nodoActual) % 2) == 0:
            costePares = costePares + nodo.costoCamino
            #print("Nodo: "+str(nodo.estado.nodoActual) +" Profundidad:"+ str(nodo.profundidad) + " Distancia: "+str(nodo.f))
        '''print(nodo.accion +"\n")
        print('\nEstoy en ' + nodo.estado.nodoActual + " tengo que visitar" +
              str(nodo.estado.listaPendientes))'''
    return costePares

def nPares(nodo):
    contPares = 0
    if nodo != None:
        contPares = nPares(nodo.nodoPadre)
        if (int(nodo.estado.nodoActual) % 2) == 0:
            contPares = contPares + 1
            #print("Nodo: "+str(nodo.estado.nodoActual) +" Profundidad:"+ str(nodo.profundidad) + " Distancia: "+str(nodo.f))
        print(nodo.accion +"\n")
        print('\nEstoy en ' + nodo.estado.nodoActual + " tengo que visitar" +
              str(nodo.estado.listaPendientes))
    return contPares

def creaSolucion(nodoActual, numNodos):

    print('Nodos generados-->' + str(numNodos))
    print('Profundidad-->' + str(nodoActual.profundidad))
    print('Costo-->' + str(nodoActual.costoCamino))
    costeP = recorreNodoPadre(nodoActual)
    numeroPares = nPares(nodoActual)
    print("\nNumero de pares en la solución: "+ str(numeroPares))
    print("Cantidad de nodos pares en solución: "+ str(costeP) + "\n")

    return True

def busquedaAcotada(prob, estrategia, profMax):
    frontera = Frontera()
    nodoInicial = NodoArbol(None, prob.estadoInicial, 0, 0, 0)
    listVisitados = []
    frontera.insert(nodoInicial)
    solucion = False

    while (solucion == False) and (not frontera.isEmpty()):
        nodoActual = frontera.delete()
        listVisitados.append((nodoActual.estado.identificador, nodoActual.f))
        if prob.esObjetivo(nodoActual.estado):
            solucion = True
        else:
            listaSucesiones = prob.espacioEstados.sucesores(nodoActual.estado)
            '''if nodoActual.estado.identificador == "a22463e1af1ae30025daf98de8c44f17":
                for i in listaSucesiones:
                    print(i[0]+" IdOSM: "+nodoActual.estado.nodoActual+" Nodos Pendientes: "+ str(nodoActual.estado.listaPendientes) + " Coste: "+ i[2] +"\n")'''
            listaNodos = creaListaNodosArbol(listaSucesiones, nodoActual, profMax, estrategia)

            for n in listaNodos:
                if not(any(n.estado.identificador == nodoRecorrido[0] for nodoRecorrido in listVisitados)): 
                    if any(n.estado.identificador == nodoFrontera.estado.identificador and n.f < nodoFrontera.f for nodoFrontera in frontera.frontera):
                        frontera.insert(n)
                    else:
                        frontera.insert(n)
                    
    if solucion == True:
        return creaSolucion(nodoActual, len(listVisitados))
    else:
        return None

def busquedaIterativa(prob, estrategia, profMax, incProf):
    profActual = incProf
    Solucion = None
    while Solucion == None and profActual <= profMax:
        Solucion = busquedaAcotada(prob, estrategia, profActual)
        profActual = profActual + incProf
    return Solucion

def menu():
    print("Seleccione la estrategia de búsqueda a usar")
    print("\t 1 - Busqueda en ANCHURA")
    print("\t 2 - Busqueda en PROFUNDIDAD SIMPLE")
    print("\t 3 - Busqueda en PROFUNDIDAD ITERATIVA")
    print("\t 4 - Busqueda por COSTE")
    print("\t 5 - Busqueda por VORAZ")
    print("\t 6 - Busqueda por A*")
    print("\t 9 - Salir")

data = open("Anchuras.json", "r")
datos = data.read()
prob = Problema(json.loads(datos))
print("MENU")
while True:
    menu()
    opcionMenu = int(input(""))

    if opcionMenu == BFS:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, BFS, profMax)
        tFinal = time.time()

        print('Estrategia--> Anchura')
        print("Tiempo total" + str(tFinal - tComienzo))

    elif opcionMenu == DFS:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1
        tComienzo = time.time()
        busquedaAcotada(prob, DFS, profMax)
        tFinal = time.time()

        print('Estrategia--> Profundidad')
        print("Tiempo total" + str(tFinal - tComienzo))

    elif opcionMenu == DFS_IT:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        print("Digame la incremento en la profundidad")
        incProf = int(input(""))

        tComienzo = time.time()
        busquedaIterativa(prob, DFS_IT, profMax, incProf)
        tFinal = time.time()

        print('Estrategia--> Profundidad Iterativa')
        print("Tiempo total" + str(tFinal - tComienzo))

    elif opcionMenu == COST:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, COST, profMax)
        tFinal = time.time()

        print('Estrategia--> Coste')
        print("Tiempo total" + str(tFinal - tComienzo))

    elif opcionMenu == VORAZ:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, VORAZ, profMax)
        tFinal = time.time()
        
        print('Estrategia--> Voraz')
        print("Tiempo total" + str(tFinal - tComienzo))

    elif opcionMenu == A:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, A, profMax)
        tFinal = time.time()

        print('Estrategia--> A*')
        print("Tiempo total" + str(tFinal - tComienzo))

    elif opcionMenu == 9:
        break