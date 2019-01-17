import json
import time

from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema
from Estado import Estado
BFS = 1
DFS = 2
DFS_IT = 3
COST = 4
VORAZ = 5
A = 6

def heuristica(nodoSucesor):
    list_distancias = []
    for n in nodoSucesor.listaPendientes:
        list_distancias.append(prob.distance(nodoSucesor.nodoActual, n))
    if not(list_distancias):
        return 0
    return min(list_distancias) 

def calcularF(estrategia, coste, profundidad, nodoActual,nodoSucesor,costeaccion):
    estadoActual=nodoActual.estado
    if estrategia == DFS:
        return -float(profundidad)
    if estrategia == DFS_IT:
        return -float(profundidad)
    elif estrategia == BFS:
        return float(profundidad)
    elif estrategia == COST:
        return coste
    elif estrategia == VORAZ:
        return heuristica(nodoSucesor)
    elif estrategia == A:
        return coste + heuristica(nodoSucesor)

def creaListaNodosArbol(listaSucesiones, nodoActual, profMax, estrategia):
    listNodosArbol = []
    for sucesion in listaSucesiones:
        profundidad = nodoActual.profundidad + 1
        if profundidad <= profMax:

            costeCamino = float(nodoActual.costoCamino) + float(sucesion[2])
            costeAccion=float(sucesion[2])
            estadoSucesor=sucesion[1]
            
            f = calcularF(estrategia, costeCamino, profundidad,nodoActual,estadoSucesor,costeAccion)

            nodoNuevo = NodoArbol(nodoActual, estadoSucesor, profundidad, costeCamino, f,costeAccion)
            listNodosArbol.append(nodoNuevo)
    return listNodosArbol
        
def print_solution(Nodos):
    for nodo in Nodos:
        print(str(nodo.accion))
        print('Estoy en ' + nodo.estado.nodoActual + " tengo que visitar" + str(nodo.estado.listaPendientes)+'\n')
#EJERCICIO C

def crearNodoSolucion(nodoAct):
    NodosSolucion = []
    NodosSolucion.append(nodoAct)
    nodo=nodoAct.nodoPadre
    while( not(nodo.nodoPadre==None)):
        NodosSolucion.append(nodo)
        nodo=nodo.nodoPadre
    NodosSolucion.append(nodo)
    # distanciaA=0
    # NodosPares=[]
    # cont=0
    NodosSolucion.reverse()
    print_solution(NodosSolucion)
    # for x in NodosSolucion:

    #     if ((int(x.estado.nodoActual)%2) == 0):
    #         NodosPares.append(x)
    #         distanciaA=distanciaA+(NodosSolucion[cont+1].costoCamino-NodosSolucion[cont].costoCamino)
    #     cont+=1
    # print("-------EJERCICIO C")
    # print("Numero total de nodos con id par "+str(len(NodosPares)))
    # print("distancia de nodos consecutivos "+str(distanciaA))

    return NodosSolucion
def print_Sucesor(estado):
    sucesiones=prob.espacioEstados.sucesores(estado)
    for sucesion in sucesiones:
        print("accion:" +str(sucesion[0]))
        print("nuevo estado:" +str(sucesion[1].listaPendientes))
        print("coste:" +str(sucesion[2]))

def creaSolucion(nodoActual, numNodos):
    a=crearNodoSolucion(nodoActual)
    print('Nodos introducidos generados-->' + str(numNodos))
    print('Profundidad-->' + str(nodoActual.profundidad))
    print('Costo-->' + str(nodoActual.costoCamino))
    return a

def busquedaAcotada(prob, estrategia, profMax):
    frontera = Frontera()
    estadoInicial=prob.estadoInicial  
    nodoInicial = NodoArbol(None, estadoInicial, 0, 0, 0,0)
    listVisitados = []
    frontera.insert(nodoInicial)
    solucion = False
    cont_nodosFrontera=0#Ejercicio B
    cont_nodosGenerados=0

    while (solucion == False) and (not frontera.isEmpty()):

        nodoActual = frontera.delete()
        listVisitados.append((nodoActual.estado.identificador, nodoActual.f))
        if prob.esObjetivo(nodoActual.estado):
            solucion = True
        else:
            listaSucesiones = prob.espacioEstados.sucesores(nodoActual.estado)
            listaNodos = creaListaNodosArbol(listaSucesiones, nodoActual, profMax, estrategia)
            cont_nodosGenerados=listaNodos.__len__()+cont_nodosGenerados
            for n in listaNodos:
                if not(any(n.estado.identificador == nodoRecorrido[0] for nodoRecorrido in listVisitados)): 
                    if any(n.estado.identificador == nodoFrontera.estado.identificador and n.costoCamino >= nodoFrontera.costoCamino for nodoFrontera in frontera.frontera):
                        pass
                    else:
                        try:
                            frontera.insert(n)
                            cont_nodosFrontera+=1
                        except Exception:
                            print("Error en la frontera")
                    
    if solucion == True:
        return creaSolucion(nodoActual, cont_nodosGenerados)
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

data = open("Almagro.json", "r")
datos = data.read()
prob = Problema(json.loads(datos))
# prueba=Estado('4331431346',['4331489575', '4331489683', '4762868814'])
# print(heuristica(prueba))
# e=Estado("2255062913",['2272379834', '2272379840'])

# print_Sucesor(e)

# print("-------EJERCICIO A")


# estadoA=Estado("326059720",["326059362"])
# sucesoresA = prob.espacioEstados.sucesores(estadoA)
# for x in sucesoresA:
#     print(x[0])
#     print(str(x[1].nodoActual))
#     print(str(x[1].listaPendientes))
#     print(str(x[2]))
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
        print(tFinal - tComienzo)

    elif opcionMenu == DFS:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1
        tComienzo = time.time()
        busquedaAcotada(prob, DFS, profMax)
        tFinal = time.time()

        print('Estrategia--> Profundidad')
        print(tFinal - tComienzo)

    elif opcionMenu == DFS_IT:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        print("Incremento profundidad")
        incProf = int(input(""))

        tComienzo = time.time()
        busquedaIterativa(prob, DFS_IT, profMax, incProf)
        tFinal = time.time()

        print('Estrategia--> Profundidad Iterativa')

    elif opcionMenu == COST:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, COST, profMax)
        tFinal = time.time()

        print('Estrategia--> Coste')
        print(tFinal - tComienzo)

    elif opcionMenu == VORAZ:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, VORAZ, profMax)
        tFinal = time.time()
        
        print('Estrategia--> Voraz')
        print(tFinal - tComienzo)

    elif opcionMenu == A:
        print("Digame la profundidad máxima")
        profMax = int(input(""))
        incProf = 1

        tComienzo = time.time()
        busquedaAcotada(prob, A, profMax)
        tFinal = time.time()

        print('Estrategia--> A*')
        print(tFinal - tComienzo)

    elif opcionMenu == 9:
        break