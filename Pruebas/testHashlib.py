import json
import hashlib
import sys

lista = ["852636538","843205891","958245069","154749196","855048479","4547812588"]
node = "154749574"
h = hashlib.md5() 
h.update("2140711440".encode())
for nodo in lista:
    h.update(nodo.encode())
print(h.hexdigest())    