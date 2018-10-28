import json
import hashlib
import sys

data = open("fichero.json", "r")
datos = data.read()
data_string = json.loads(datos)

node = data_string['IntSt']['node']
lista = data_string['IntSt']['listNodes']
h = hashlib.md5() 
h.update(node.encode())
for nodo in lista:
    h.update(nodo.encode())
print(h.hexdigest())