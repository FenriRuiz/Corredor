from EspacioEstados import EspacioEstados
from Estado import Estado

class Problema:
    def __init__(self,json):
        self.espacioEstados=EspacioEstados(json['graphlmfile'])
        self.estadoInicial=Estado(json['IntSt']['node'], json['IntSt']['listNodes'])
    def esObjetivo(self, Estado):
        if(not Estado.listaPendientes):
            return True
        else:
            return False

