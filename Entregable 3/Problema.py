from EspacioEstados import EspacioEstados
from Estado import Estado
import math

class Problema:
    def __init__(self, json):
        self.espacioEstados = EspacioEstados(json['graphlmfile'])
        self.estadoInicial = Estado(json['IntSt']['node'], json['IntSt']['listNodes'])

    def esObjetivo(self, Estado):
        if not Estado.listaPendientes:
            return True
        else:
            return False

    def distance(self, idNode1, idNode2):
        (lng1, lat1) = self.espacioEstados.lonlat(idNode1)
        (lng2, lat2) = self.espacioEstados.lonlat(idNode2)

        earth_radius = 6371009

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        d_phi = phi2 - phi1

        theta1 = math.radians(lng1)
        theta2 = math.radians(lng2)

        d_theta = theta2 - theta1
        
        h = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_theta / 2) ** 2
        h = min(1.0, h) #protect against floating point errors

        arc = 2 * math.asin(math.sqrt(h))
        #return distance in units of earth radius
        dist = arc * earth_radius
        return dist

