import json
import hashlib
import sys

#     "node": "4331431334", 
#     "listNodes": ["4331489575", "4331489683", "4762868814"], 
#     "id": "22bd7e5aa38ce7e9f8926fbd71383989"}}

lista =  ["1675756709", "1809811393"]
node = "1675746635"
h = hashlib.md5() 
h.update(node.encode())
for nodo in lista:
    h.update(nodo.encode())

print(h.hexdigest())    