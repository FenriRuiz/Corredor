
class Alumno:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

frontera=[]

frontera.append(Alumno("Fernando", 23, 3))
frontera.append(Alumno("Alejandro", 10, 1))
frontera.append(Alumno("Rafael", 21, 4))

print("Frontera Sin Ordenar")

for i in frontera:
    print(i.nombre+" "+str(i.edad)+" "+ str(i.curso))

print("\nFrontera Ordenada")
frontera.sort(key = lambda x: x.edad)

for i in frontera:
    print(i.nombre+" "+str(i.edad)+" "+ str(i.curso))