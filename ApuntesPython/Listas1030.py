# las listas son estructuras de datos lineales
# Se crean usando brackes ej: my_list = []
# las listas son ordenadas (Orden de insersion), esto quiere dicr
# que el ultimo dato ingresado ocupará la ultima posición.
# Emplea métodos para manipular los items de la misma.
# Como los array la primera posicion inicia en 0
# Permite items duplicados.
# Las listas son mutables, es decir podemos agregar , actualizar o remover items
# Puede contener distintos tipos de datos



nombres= ["Pepito", "Andres", "Juan", "Maria", "Pedro"]
edades = [25,19,21,33,40]
estaturas = [1.80, 1.65,1.74,1.66,1.54]
casados = [False,False,False,True,True]
usuario = ["Pepito",25,1.80,False]


print(nombres[0], edades[0],estaturas[0],casados[0])

print(len(edades))

print(type(nombres))
print(type(edades))
print(type(estaturas))
print(type(casados))
print(type(usuario))

#Slice --- Rangos en la lista

print(usuario[0:3])
print(nombres[1:3])
print(nombres[:3])
print(nombres[1:])
print(nombres[:-1])
print(nombres[:4])
print(nombres[-4:-1])
print(nombres[1:4])

# Podemos validar si existe en la lista algun elemento

if "pepito" in nombres:
    print(f"el nombre esta en la lista")
else:
    print("NO se encontro el nombre buscado") 

usuario[0]= "Luis"
print(usuario[0])   

nombres[0:3]= "Luis","Pablo","Pipe"   
print(nombres[0:5])

# Queremos insertar un item en una posicion especifica => insert(i,value)

nombres.insert(0,"Pepito")
print(nombres[0:])
# Podemos agregar con el metodo append() items, pero este se agrega al final de la lista
nombres.append("Laura")
print(nombres[0:])

nombres2= ["Lis", "Ana"]

listPrueba = nombres.extend(nombres2)
print(nombres[0:])
print(type(nombres))
nombres.remove("Pipe")
print(nombres[0:])
nombres.remove("Lis")
print(nombres[0:])
nombres.pop(4)
print(nombres[0:])
del nombres[1]
print(nombres[0:])
nombres.clear()
print(nombres[0:])
del nombres
#print(nombres[0:])


#Recorriendo listas 

for i in edades:
    print(i)

#Iterar en los index


for i in range (len(estaturas)):
    print(estaturas[i])

# Iterar la lista usando while

i = 0

while i<len(usuario):
    print(usuario[i])
    i += 1

# List Comprehension

print("------------------")

[print(x) for x in usuario]

print("------------------")

for i, edad in enumerate(edades):

    print(i, edad)