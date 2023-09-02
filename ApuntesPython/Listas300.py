# las listas son estructuras de datos lineales
# Se crean usando brackes ej: my_list = []
# las listas son ordenadas (Orden de insersion), esto quiere dicr
# que el ultimo dato ingresado ocupará la ultima posición.
# Emplea métodos para manipular los items de la misma.
# Como los array la primera posicion inicia en 0
# Permite items duplicados.
# Las listas son mutables, es decir podemos agregar , actualizar o remover items
# Puede contener distintos tipos de datos

materias = ["Matematica", "Español " ,"Ciencias","Sociales","Fisica", "quimica"]

#Para deteminar el tamaño de la lista podemos usar len()
print(len(materias))

#print(dir(materias))

#POdemos acceder a los elementos indicando la posicion:

print(materias[2])

#Slicing muestra las posiciones en un rango

print(materias[2:5])

print(materias[3:])

print(materias[:5])

print(materias[-5:-1])
print(materias[1:5])


# Tipos de datos en las listas

edades=[17,27, 42,31,56,68]

print(type(edades))

#Actualizar un elemento de la lista

materias[2]= "Biologia"

print(materias[0:])

materias[1:3] = "Lenguaje","Ciencias Naturales"

print(materias[0:])

#Agregando Elementos a la lista

materias.append("Religion")
print(materias[0:])

materias.insert(0,"Etica")
print(materias[0:])


#Quitar elementos de la lista

materias.pop()
print(materias[0:])

materias.remove("Etica")
print(materias[0:])

del materias[4]
print(materias[0:])

#materias.clear()
#print(materias[0:])

#del materias
#print(materias[0:])

# Iterar las listas con el ciclo for



print("--------------------------") 

for i in materias:
    print(i)

print("-"*50)   


for i in range(len(materias)):
    print(materias[i])

print("-"*50)

for i, materia in enumerate(materias):
    print(i, materia)

print("-"*50) 


#Usando un ciclo while

i= 0

while i < len(materias):
    print(materias[i])
    i+= 1

print("-"*50)  

# List Comprehension

[print(i) for i in materias]

#crear lista numero

numeros = [numero for numero in range(1,31)]

print(numeros)