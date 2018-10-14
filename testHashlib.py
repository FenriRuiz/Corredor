import json
import hashlib
import sys

lista = ["4331489528","4331489668","4331489711","4762868815","4928063625"]
node = "4331489739"
h = hashlib.md5() 
h.update("4331489739".encode())
for nodo in lista:
    h.update(nodo.encode())
print(h.hexdigest())