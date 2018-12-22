import json
import hashlib
import sys

lista = ["1113332522","326059362","163888636","1005669685","1911227547"]
node = "1113332475"
h = hashlib.md5() 
h.update("1113332475".encode())
for nodo in lista:
    h.update(nodo.encode())
print(h.hexdigest())    