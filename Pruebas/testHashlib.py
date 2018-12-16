import json
import hashlib
import sys

lista = ["960815541","325794463"]
node = "2140711440"
h = hashlib.md5() 
h.update("2140711440".encode())
for nodo in lista:
    h.update(nodo.encode())
print(h.hexdigest())    